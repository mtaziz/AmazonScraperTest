# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class AnzSpiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import csv
import itertools

import requests
from scrapy.utils.project import get_project_settings
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
import json
from scrapy.conf import settings
SETTINGS = get_project_settings()

class AnzSpiderPipeline(object):

  def __init__(self):
        self.files = {}

  @classmethod
  def from_crawler(cls, crawler):
        pipeline = cls()
        return pipeline

  def process_item(self, item, spider):
        file = open('%s_items.json' % spider.name, 'w+b')
        self.files[spider] = file
        file.write('{"anzbank":')
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()
        self.exporter.export_item(item)
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.write("}")
        file.close()
        return item


class CSVPipeline(object):
	def __init__(self):
		self.csvwriter = csv.writer(open('items.csv', 'wb'), delimiter=',')
		self.csvwriter.writerow([ 'UK_Plan_Name','UK_Plan_Bundle_Price','Plan_Validity','National_Mins', 'National_Text', 'National_Data'])
		# self.csvwriter.writerow([ 'Source_Urls', 'UK_Plan_Name','UK_Plan_Bundle_Price','Plan_Validity','National_Mins', 'National_Text', 'National_Data'])
		# self.csvwriter.writerow([ 'UK_Plan_Name','Plan_Validity','National_Mins', 'National_Text', 'National_Data'])
	
	# def process_item(self, item, spider):
	# 	rows = zip(item['Source_Urls'],item['UK_Plan_Name'],item['UK_Plan_Bundle_Price'],item['Plan_Validity'],item['National_Mins'],item['National_Text'],item['National_Data'])
	def process_item(self, item, spider):
		rows = zip([item['UK_Plan_Name'],item['UK_Plan_Bundle_Price'],item['Plan_Validity'],item['National_Mins'],item['National_Text'],item['National_Data']])
	# def process_item(self, item, spider):
	# 	rows = zip(item['UK_Plan_Name'],item['Plan_Validity'],item['National_Mins'],item['National_Text'],item['National_Data'])

		for row in rows:
			self.csvwriter.writerow(row)
		return item