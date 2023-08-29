# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TftItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #info de producto
    summoner = scrapy.Field()
    lps = scrapy.Field()
    wins = scrapy.Field()
    tops = scrapy.Field()
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
    lastDay = scrapy.Field()
    tier = scrapy.Field()
