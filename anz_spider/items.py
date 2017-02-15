# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


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


class BankNameSpiderItem(scrapy.Item):
	Name = scrapy.Field()
