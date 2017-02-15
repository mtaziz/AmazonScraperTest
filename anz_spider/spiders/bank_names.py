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

from anz_spider.items import BankNameSpiderItem
# from import


class ListOfBanksSpider(scrapy.Spider):
	name = 'bank_names'
	allowed_domains = ['thebsbnumbers.com']
	start_urls = ['https://www.thebsbnumbers.com']

	"""
	custom settings which overides crawlera settings
	"""
	custom_settings = {'FIELDS_TO_EXPORT': ['Name'],'DOWNLOAD_DELAY': 30.0}
	# def start_requests(self):
	# 	for i in range(1, 27):
	# 		url = 'https://www.thebsbnumbers.com/anz-bank/page/%s/' % i
	# 		yield self.make_requests_from_url(url)
	# 		# yield scrapy.Request(url, dont_filter=True)
	
	def parse(self, response):
		item = BankNameSpiderItem()
		items = []
		# /html/body/div[3]/div[2]/ul[2]
		for i in response.xpath('//ul[2]/li'):
			 name_data = i.xpath('.//a/@href').extract_first()
			 name_data = ''.join(name_data).strip()
			 name_data = re.findall(r'\w.+[^/]', name_data)
			 item['Name'] = name_data
			 yield item
			# items.append(item)
		# return items
			# yield item