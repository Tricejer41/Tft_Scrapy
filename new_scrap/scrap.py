from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from tqdm import tqdm
import multiprocessing
import os

# Configuración del driver
CHROMEDRIVER_PATH = r"C:\\Users\\Tricejer\\Desktop\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"  # Cambia esta ruta a la ubicación de tu ChromeDriver

# Función para obtener los jugadores de una página del leaderboard
def get_players_from_leaderboard(driver, page, tier, region):
    url = f"https://lolchess.gg/leaderboards?region={region}&mode=ranked&tier={tier}&page={page}"
    driver.get(url)
    time.sleep(5)  # Espera para evitar bloqueos

    players = []
    rows = driver.find_elements(By.CSS_SELECTOR, "table.ReactTable tbody tr")

    print(f"Página {page} en {tier} ({region}): Encontrados {len(rows)} jugadores.")

    for row in rows:
        try:
            nickname_elem = row.find_element(By.CSS_SELECTOR, "td.summoner a")
            tier_elem = row.find_element(By.CSS_SELECTOR, "td.tier .tier-text")
            lp_elem = row.find_element(By.CSS_SELECTOR, "td.lp .tier-text")

            nickname = nickname_elem.text.strip()
            profile_url = nickname_elem.get_attribute("href")
            tier_text = tier_elem.text.strip()
            lp = lp_elem.text.strip()
            players.append({"nickname": nickname, "profile_url": profile_url, "tier": tier_text, "lp": lp, "region": region})
        except Exception as e:
            print(f"Error procesando un jugador: {e}")

    return players

# Función para obtener datos del perfil del jugador
def get_player_profile_data(driver, profile_url):
    try:
        driver.get(profile_url)
        time.sleep(5)  # Espera para evitar bloqueos

        # Comprobar si los campeones están presentes
        champions_data = []
        champion_rows = driver.find_elements(By.CSS_SELECTOR, "div.StatisticTable div.data > div")
        for row in champion_rows[:5]:  # Top 5 campeones
            try:
                champ_name_elem = row.find_element(By.CSS_SELECTOR, "div.label .name a")
                games_played_elem = row.find_element(By.CSS_SELECTOR, "div.plays")

                champ_name = champ_name_elem.text.strip()
                games_played = int(games_played_elem.text.strip())
                champions_data.append({"champion": champ_name, "games_played": games_played})
            except Exception as e:
                print(f"Error procesando campeón: {e}")

        # Número de victorias y TOP 4 en las últimas 20 partidas
        wins_elem = driver.find_element(By.CSS_SELECTOR, "div.info.wins strong.wins")
        top4_elem = driver.find_element(By.CSS_SELECTOR, "div.info.top strong.top")

        return {
            "top_champions": champions_data,
            "wins": int(wins_elem.text.strip()) if wins_elem else 0,
            "top4": int(top4_elem.text.strip()) if top4_elem else 0,
        }
    except Exception as e:
        print(f"Error procesando el perfil {profile_url}: {e}")
        # Tomar captura de pantalla para análisis
        safe_profile_id = profile_url.split('/')[-1] if '/' in profile_url else "unknown"
        driver.save_screenshot(f"error_{safe_profile_id}.png")
        return {}

# Función para procesar una región completa
def process_region(region, tiers, output_queue):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar en modo headless (sin abrir navegador)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    
    players_data = []
    
    try:
        for tier, max_pages in tiers.items():
            for page in tqdm(range(1, max_pages + 1), desc=f"Páginas de clasificación ({tier}, {region})", position=0):
                players = get_players_from_leaderboard(driver, page, tier, region)
                for player in tqdm(players, desc=f"Jugadores en página {page} ({tier}, {region})", position=1, leave=False):
                    profile_data = get_player_profile_data(driver, player['profile_url'])

                    # Estructurar datos de campeones
                    top_champions = profile_data.get('top_champions', [])
                    player_data = {
                        "nickname": player['nickname'],
                        "region": player['region'],
                        "tier": player['tier'],
                        "lp": player['lp'],
                        "wins": profile_data.get('wins', 0),
                        "top4": profile_data.get('top4', 0),
                    }
                    # Añadir campeones al diccionario
                    for i, champ in enumerate(top_champions):
                        player_data[f"champ_{i+1}"] = champ["champion"]
                        player_data[f"games_champ_{i+1}"] = champ["games_played"]

                    # Si no hay 5 campeones, rellenar con None
                    for i in range(len(top_champions), 5):
                        player_data[f"champ_{i+1}"] = None
                        player_data[f"games_champ_{i+1}"] = None

                    players_data.append(player_data)
    finally:
        driver.quit()
    
    # Poner los datos recopilados en la cola para ser recogidos por el proceso principal
    output_queue.put(players_data)

# Función principal
def main():
    manager = multiprocessing.Manager()
    output_queue = manager.Queue()
    
    regions = {
        "euw": {"challenger": 2, "grandmaster": 4, "master": 10},
        "jp": {"challenger": 2, "grandmaster": 4, "master": 10},
        "kr": {"challenger": 2, "grandmaster": 4, "master": 10},
        "na": {"challenger": 2, "grandmaster": 4, "master": 10},
    }

    processes = []
    for region, tiers in regions.items():
        p = multiprocessing.Process(target=process_region, args=(region, tiers, output_queue))
        processes.append(p)
        p.start()
        print(f"Proceso iniciado para la región: {region}")

    # Recoger todos los datos de los procesos
    all_players_data = []
    for _ in regions:
        all_players_data.extend(output_queue.get())

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()
        print(f"Proceso finalizado para la región: {p.name}")

    # Guardar los datos en un CSV
    df = pd.DataFrame(all_players_data)
    df.to_csv("tft_player_data_global.csv", index=False)
    print("Datos guardados en 'tft_player_data_global.csv'.")

if __name__ == "__main__":
    main()
