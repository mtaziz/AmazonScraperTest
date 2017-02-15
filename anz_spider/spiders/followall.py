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


class AnzSpider(scrapy.Spider):
	name = 'anz'
	allowed_domains = ['thebsbnumbers.com']

	"""
	custom settings which overides crawlera settings
	"""
	# custom_settings = {'CRAWLERA_PRESERVE_DELAY': True,'DOWNLOAD_DELAY': 1.0}
	bank_list = ['adelaide-bank', 'advance-bank', 'amp-bank', 'anz-bank', 'arab-bank-australia', 'auswide-bank', '', 
				'bank-of-america', 'bank-of-china', 'bank-of-communications', 'bank-of-melbourne', 'bank-of-queensland', 
				'bank-of-sydney', 'bank-of-tokyo-mitsubishi-ufj', 'bankmecu', 'banksa', 'bankwest', 'bendigo-and-adelaide-bank', 
				'beyond-bank', 'bnp-paribas', 'boq-specialist', 'capricornian', 'china-construction-bank', 'citibank', 'commonwealth-bank', 
				'defence-bank', 'delphi-bank', 'deutsche-bank', 'gc-mutual-bank', 'heritage-bank', 'hsbc-bank', 'hume-bank', 
				'industrial-and-commercial-bank-of-china', 'ing-bank', 'jp-morgan-chase-bank', 'macquarie-bank', 
				'mega-international-commercial-bank', 'members-equity-bank', 'mizuho-bank', 'national-australia-bank', 
				'ocbc-bank', 'pn-bank', 'police-bank', 'qt-mutual-bank', 'rabobank', 'reserve-bank-of-australia', 
				'st-george-bank', 'sumitomo-mitsui-banking-corporation', 'suncorp', 'taiwan-business-bank', 
				'teachers-mutual-bank', 'the-royal-bank-of-scotland', 'ubs', 'united-overseas-bank', 'westpac-bank']

				
	def start_requests(self):
		for i in range(1, 27):
			url = 'https://www.thebsbnumbers.com/anz-bank/page/%s/' % i
			yield self.make_requests_from_url(url)
			# yield scrapy.Request(url, dont_filter=True)
	
	def parse(self, response):
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

# URL = scrapy.Field()
#     No = scrapy.Field()
#     Bank = scrapy.Field()
#     State = scrapy.Field()
#     City = scrapy.Field()
#     Branch = scrapy.Field()
#     Street = scrapy.Field()
#     BSB = scrapy.Field()

	# category_urls = ['electronics-goods',
	# 	'home-and-garden-goods',
	# 	'women',
	# 	'men',
	# 	'baby-kids-and-toys',
	# 	'jewellery-and-watches',
	# 	'health-and-beauty-goods',
	# 	'sports-and-outdoors',
	# 	'grocery-alcohol-and-tobacco',
	# 	'entertainment-goods',
	# 	'auto-and-home-improvement']

	# groupon_uk_start_urls = ['https://www.groupon.co.uk/goods/electronics-goods',
	# 	'https://www.groupon.co.uk/goods/home-and-garden-goods',
	# 	'https://www.groupon.co.uk/goods/women',
	# 	'https://www.groupon.co.uk/goods/men',
	# 	'https://www.groupon.co.uk/goods/baby-kids-and-toys',
	# 	'https://www.groupon.co.uk/goods/jewellery-and-watches',
	# 	'https://www.groupon.co.uk/goods/health-and-beauty-goods',
	# 	'https://www.groupon.co.uk/goods/sports-and-outdoors',
	# 	'https://www.groupon.co.uk/goods/grocery-alcohol-and-tobacco',
	# 	'https://www.groupon.co.uk/goods/entertainment-goods',
	# 	'https://www.groupon.co.uk/goods/auto-and-home-improvement']

  #### Test single url without link extraction
  # start_urls = ['https://www.groupon.co.uk/deals/gg-groupon-goods-global-gmb-h-5-4153']

	# for url in category_urls:
	# 	print url
	# 	for i in range(1, 20):
	# 		groupon_uk_start_urls.append('https://www.groupon.co.uk/goods/%s?page=%s' % (url, i))
	# start_urls = gro upon_uk_start_urls

### find deals then parse it
	# rules = (
	# 	Rule(
	# 		LinkExtractor(
	# 			allow=(r'\/deals\/\w.+',),
	# 			# restrict_xpaths=('//li[@class="next"]',),
	# 			unique=True,),
	# 		callback='parse_item_detail',),
	# )

  ### For only testing purpose if Crawlspider does not work, use Spider and parse function for a single "start_urls"
  # def parse(self, response):


	# def parse_item_detail(self, response):
	# 	item = GrouponUkItem()
	# 	name_data = response.xpath('//meta[@name="description"]/@content').extract_first()
	# 	if name_data:
	# 		item['name'] = name_data.encode('ascii', errors='ignore')
	# 	else:
	# 		item['name'] = ''
	# 	# response.xpath('//meta[@property="og:title"]/@content').extract()
	# 	# //*[@id="deal-title"]/text()
	# 	item['country'] = 'UK'
	# 	price_data = response.xpath('//*[@id="deal-hero-price"]/div/span/text()').extract_first()
	# 	#GBP symbol taken off
	# 	if price_data:
	# 		price_data_clean = ''.join(price_data).encode('ascii', 'ignore')
	# 		item['price'] = price_data_clean
	# 	else:
	# 		item['price'] = ''
	# 	item['category_old'] = ''
	# 	item['image_url'] = response.xpath('//meta[@property="og:image"]/@content').extract_first()
	# 	# interest_data = response.xpath('//div[contains(@class, "urgency-message")]/span/span[@class="qty-msg"]/text()').extract()
	# 	# interest_data = response.xpath('//*[starts-with(@class,"qty-")]/text()').extract()
	# 	interest_data = ''.join(response.xpath('//*[starts-with(@class,"qty-")]/text()').re(r'\d+'))
	# 	if interest_data:
	# 		item['interest'] = interest_data
	# 	else:
	# 		item['interest'] = ''
	# 		# for s in str(interest_data).split():
	# 		# 	if s.isdigit():
	# 		# 		item['interest'] = int(s)
	# 		# 		if not s.isdigit():
	# 		# 			item['interest'] = ''
	# 		# 	else:
	# 		# 		item['interest'] = ''
	# 			# else:
	# 			# 	item['interest'] = ''
	# 	# if not interest_data:
	# 	# 	item['interest'] = ''
	# 	item['link'] = response.url
	# 	item['company'] = 'Groupon UK'
	# 	item['start_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	# 	# item['country'] = 'UK'
	# 	item['type'] = 'Dailydeal'
	# 	item['currency'] = 'GBP'
	# 	###Scraped time
	# 	#item['indexedDate'] = [datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")]
	# 	#dateTimeString = datetime.utcnow().strftime("%Y%m%d_%H:%M%S")
		
	# 	return item
