# -*- coding: utf-8 -*-
# import scrapy


# class AnzSpider(scrapy.Spider):
#     name = "anz"
#     allowed_domains = ["https://www.thebsbnumbers.com/"]
#     start_urls = (
#         'http://www.https://www.thebsbnumbers.com//',
#     )

#     def parse(self, response):
#         pass
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
import requests
from scrapy.conf import settings
from scrapy import Selector
from time import strftime, strptime, gmtime
from datetime import datetime
from urlparse import urljoin
from anz_spider.items import AnzSpiderItem
# from import

class AnzSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    URL = scrapy.Field()
    No = scrapy.Field()
    Bank = scrapy.Field()
    State = scrapy.Field()
    City = scrapy.Field()
    Branch = scrapy.Field()
    Street = scrapy.Field()
    BSB = scrapy.Field()


class AnzAdvancedSpider(CrawlSpider):
	name = 'anz_advanced'
	allowed_domains = ['thebsbnumbers.com']
	start_urls = ['https://www.thebsbnumbers.com/']

	def parse(self, response):
		sel = Selector(response)
		sites = sel.xpath('//ul[2]/li//a/@href').extract()
		for site in sites:
			yield scrapy.Request(''.join(['https://www.thebsbnumbers.com', site]), callback=self.parse_pages, dont_filter=True)

	def parse_pages(self, response):
		# sel = Selector(response)
		page_num = len(response.xpath('//div[contains(@class, "post_")]/div[2]/span').extract())
		print page_num
		for i in range(1, page_num):
			pg_url = urljoin(response.url, '/page/%s/' % i)
			print pg_url
			yield scrapy.Request(pg_url, callback=self.parse_items) 
			# url = 'https://www.thebsbnumbers.com/anz-bank/page/%s/' % i


	# """
	# custom settings which overides crawlera settings
	# """
	# # custom_settings = {'CRAWLERA_PRESERVE_DELAY': True,'DOWNLOAD_DELAY': 1.0}
	# # /html/body/div[3]/div[1]/div/div[4]/div[2]
	# def start_requests(self):
	# 	# pages_numbers = response.xpath('//div[contains(@class, "post_")]/div[2]/span').extract()
	# 	for i in range(1, 27):
	# 		url = 'https://www.thebsbnumbers.com/anz-bank/page/%s/' % i
	# 		yield self.make_requests_from_url(url)
			# yield scrapy.Request(url, dont_filter=True)
	
	def parse_items(self, response):
		# sel = Selector(response)
		# item['URL'] = response.url
		for s in response.xpath('//tr'):
			item = AnzSpiderItem()
			item['URL'] = response.url
			items = []
			# s = sector(response)
			# No_xpath = /html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[2]
			# 			 /html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[3]/td[2]
			###{{{Raw#Attempt#1
			# item['No'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[2]/text()').extract()
			# item['Bank'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[3]/text()').extract()
			# item['State'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[4]').extract()

			# item['City'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[5]/text()').extract()
			# item['Branch'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[6]/text()').extract()
			# item['Street'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[7]/text()').extract()
			# item['BSB'] = response.xpath('/html/body/div[3]/div[1]/div/div[4]/table/tbody/tr[2]/td[8]/a/text()').extract()
			###End of Attempt#1 }}}
			
			###{{{Attempt#2
			item['No'] = s.xpath('.//td[2]/text()').extract()
			item['Bank'] = s.xpath('.//td[3]/text()').extract()
			item['State'] = s.xpath('.//td[4]/text()').extract()

			item['City'] = s.xpath('.//td[5]/text()').extract()
			item['Branch'] = s.xpath('.//td[6]/text()').extract()
			item['Street'] = s.xpath('.//td[7]/text()').extract()
			item['BSB'] = s.xpath('.//td[8]/a/text()').extract()
			yield item
			# items.append(item)
			# return item
		# return item 
# class SongciSpider(Spider):
#     name = "spider1"
#     allow_domains = ["songci.org"] #?
#     start_urls = ["http://ts300.5156edu.com/sc300/"]
    
#     def parse(self, response):
#         sel = Selector(response)
#         sites = sel.xpath('//table[@bgcolor="#808080"]/table/tr/td[@width="33%"]/a/@href').extract()

#         for site in sites:
#             yield scrapy.Request(''.join(["http://ts300.5156edu.com/sc300/",site]),callback=self.parse_dep2)

#     def parse_dep2(self,response):
#         sel = Selector(response)
#         item = SongciItem()
#         contents = response.xpath('//table[@id="table1"]/tr/td[@class="font_14"]')
#         item["url"] = response.url
#         item['author'] = contents.xpath('text()')[0].extract().split()[0]
#         item['title'] = contents.xpath('b/text()')[0].extract()
#         item['content'] = ''
#         contents_text = contents.xpath('text()')
#         del contents_text[0]
#         for xcontent in contents_text:
#             item['content'] = ''.join([item['content'],xcontent.extract().strip(),'\r\n'])
#         item['content'] = item['content'].strip('\r\n')
#         return item

        
