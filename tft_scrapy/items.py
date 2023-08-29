# -*- coding: utf-8 -*-

# Define aquí los modelos para tus elementos extraídos
#
# Consulta la documentación en:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TFTChampionData(scrapy.Item):
    # Define los campos para tu elemento aquí, por ejemplo:
    # nombre = scrapy.Field()

    # Información del jugador
    summoner = scrapy.Field()
    lps = scrapy.Field()
    wins = scrapy.Field()
    tops = scrapy.Field()

    # Información sobre los campeones más jugados
    firstChampName = scrapy.Field()
    firstChampPlays = scrapy.Field()
    secondChampName = scrapy.Field()
    secondChampPlays = scrapy.Field()
    thirdChampName = scrapy.Field()
    thirdChampPlays = scrapy.Field()
    fourthChampName = scrapy.Field()
    fourthChampPlays = scrapy.Field()
    fifthChampName = scrapy.Field()
    fifthChampPlays = scrapy.Field()

    # Información adicional
    lastDay = scrapy.Field()
    tier = scrapy.Field()
