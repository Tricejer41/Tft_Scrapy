# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tft.items import TftItem

class TftSpider(CrawlSpider):
	name = 'tft'
	item_count = 0
	allowed_domain = ['lolchess.gg']
	start_urls = ['https://lolchess.gg/leaderboards?mode=ranked&region=kr']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths=(['.//ul[@class="pagination"]/li[1]/a',
                                  './/ul[@class="pagination"]/li[2]/a',
                                  './/ul[@class="pagination"]/li[3]/a',
                                  './/ul[@class="pagination"]/li[4]/a',
								  './/ul[@class="pagination"]/li[5]/a',
                                  './/ul[@class="pagination"]/li[6]/a',
                                  './/ul[@class="pagination"]/li[7]/a',
								  './/ul[@class="pagination"]/li[8]/a',
                                  './/ul[@class="pagination"]/li[9]/a',
                                  './/ul[@class="pagination"]/li[10]/a']))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//td[@class="summoner"]/a')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = TftItem()
		#info de producto
		ml_item['lastDay'] = response.xpath('normalize-space(//div[@class="profile__match-history-v2__items"]/div[19]/div[1]/div[@class="age"])').extract_first()
		ml_item['summoner'] = response.xpath('normalize-space(//div[@class="player-name"]/text())').extract()
		ml_item['lps'] = response.xpath('normalize-space(//div[@class="profile__tier__summary__lp"]/text())').extract()
		ml_item['wins'] = response.xpath('normalize-space(//div[@class="profile__placements"]/div/div/dl[@class="wins"]/dd/text())').extract()
		ml_item['tops'] = response.xpath('normalize-space(//div[@class="profile__placements"]/div/div/dl[@class="top"]/dd/text())').extract()
		ml_item['firstChampName'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[1]/td[@class="name"]/a/text())').extract()
		ml_item['firstChampPlays'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[1]/td[@class="plays"]/text())').extract()
		ml_item['secondChampName'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[2]/td[@class="name"]/a/text())').extract()
		ml_item['secondChampPlays'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[2]/td[@class="plays"]/text())').extract()
		ml_item['thirdChampName'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[3]/td[@class="name"]/a/text())').extract()
		ml_item['thirdChampPlays'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[3]/td[@class="plays"]/text())').extract()
		ml_item['fourthChampName'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[4]/td[@class="name"]/a/text())').extract()
		ml_item['fourthChampPlays'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[4]/td[@class="plays"]/text())').extract()
		ml_item['fifthChampName'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[5]/td[@class="name"]/a/text())').extract()
		ml_item['fifthChampPlays'] = response.xpath('normalize-space(//div[@class="profile__recent__trends__units"]/table/tbody/tr[5]/td[@class="plays"]/text())').extract()
		ml_item['tier'] = response.xpath('normalize-space(//span[@class="profile__tier__summary__tier text-challenger"]/text())').extract()
		self.item_count += 1
		if self.item_count > 1000:
			raise CloseSpider('item_exceeded')
		yield ml_item
