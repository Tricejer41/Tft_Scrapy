import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from TFTChampionData.items import TFTChampionDataItem

class TFTChampionSpider(CrawlSpider):
    name = 'tft_champion'
    item_count = 0
    allowed_domain = ['lolchess.gg']
    start_urls = ['https://lolchess.gg/leaderboards?mode=ranked&region=kr']

    rules = {
        # Para cada elemento
        Rule(LinkExtractor(allow=(), restrict_xpaths=(
            './/ul[@class="pagination"]/li/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//td[@class="summoner"]/a')),
             callback='parse_item', follow=False)
    }

    def parse_item(self, response):
        item = TFTChampionDataItem()
        # Información del producto
        item['lastDay'] = response.xpath(
            'normalize-space(//div[@class="profile__match-history-v2__items"]/div[19]/div[1]/div[@class="age"])').extract_first()
        item['summoner'] = response.xpath(
            'normalize-space(//div[@class="player-name"]/text())').extract()
        item['lps'] = response.xpath(
            'normalize-space(//div[@class="profile__tier__summary__lp"]/text())').extract()
        item['wins'] = response.xpath(
            'normalize-space(//div[@class="profile__placements"]/div/div/dl[@class="wins"]/dd/text())').extract()
        item['tops'] = response.xpath(
            'normalize-space(//div[@class="profile__placements"]/div/div/dl[@class="top"]/dd/text())').extract()
        item['firstChampName'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[1]/td[@class="name"]/a/text())').extract()
        item['firstChampPlays'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[1]/td[@class="plays"]/text())').extract()
        item['secondChampName'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[2]/td[@class="name"]/a/text())').extract()
        item['secondChampPlays'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[2]/td[@class="plays"]/text())').extract()
        item['thirdChampName'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[3]/td[@class="name"]/a/text())').extract()
        item['thirdChampPlays'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[3]/td[@class="plays"]/text())').extract()
        item['fourthChampName'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[4]/td[@class="name"]/a/text())').extract()
        item['fourthChampPlays'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[4]/td[@class="plays"]/text())').extract()
        item['fifthChampName'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[5]/td[@class="name"]/a/text())').extract()
        item['fifthChampPlays'] = response.xpath(
            'normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[5]/td[@class="plays"]/text())').extract()
        item['tier'] = response.xpath(
            'normalize-space(//span[@class="profile__tier__summary__tier text-challenger"]/text())').extract()
        self.item_count += 1
        if self.item_count > 1000:
            raise CloseSpider('item_exceeded')
        yield item
