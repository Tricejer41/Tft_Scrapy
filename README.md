# Proyecto Scrapy TFTChampionData

![Logo de Scrapy](https://repository-images.githubusercontent.com/529502/dab2bd00-0ed2-11eb-8588-5e10679ace4d)

## Descripción

TFTChampionData es un proyecto Scrapy diseñado para recopilar datos de jugadores y campeones de TFT (Teamfight Tactics) desde el sitio web [lolchess.gg](https://lolchess.gg/). El proyecto extrae información valiosa sobre el rendimiento de los jugadores y sus campeones en el modo clasificado.

## Estructura del Proyecto

- `TFT_Meta/` - Directorio raíz del proyecto.
  - `tft_items` - Archivo con los resultados del scrapping.
  - `scrapy.cfg` - Archivo de configuración de Scrapy.
  - `tft/` - Directorio principal del proyecto.
    - `items.py` - Definiciones de elementos de datos.
    - `middlewares.py` - Middleware del proyecto (opcional).
    - `pipelines.py` - Pipelines para el procesamiento de datos.
    - `settings.py` - Configuraciones del proyecto Scrapy.
    - `spiders/` - Directorio que contiene las arañas del proyecto.
      - `__init__.py` - Archivo de inicialización de arañas.
      - `spider.py` - Araña que realiza la extracción de datos.

