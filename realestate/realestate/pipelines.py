# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter


class RealestatePipeline(object):
    def process_item(self, item, spider):
		if spider.name == 'past_realestate':
			if not item['sold_date'] or item['sold_date'] == 'N/A':
				raise DropItem("No date in %s" %item['address'])
		if len(item['bathrooms']) > 1:
			raise DropItem("Multiple bathroom inputs in %s" %item['address'])
		#elif "Other" in item['propertyType'] or "Residential Land" in item['propertyType']:
			#raise DropItem("Land  in %s" %item['address'])
		else:
			return item

class EmptycarPipeline(object):
	def process_item(self, item, spider):
		if not item['car']:
			item['car'] = 0
		if not item['bedrooms']:
			item['bedrooms'] = 0
		if not item['bathrooms']:
			item['bathrooms'] = 0
		if spider.name == 'past_realestate':
			if not item['price']:
				raise DropItem("No price ins %s"%item['address'])
		return item
		
class RequestPipeline(object):
	def process_item(self, item, spider):
		if 'request' in ''.join(item['address']):
			raise DropItem('No address given')
		else:
			return item

class DuplicatesPipeline(object):

	def __init__(self):
		self.ids_seen = set()

	def process_item(self, item, spider):
		if spider.name == 'past_realestate':
			str1 = ''.join(item['address'])
			str2 = ''.join(item['sold_date'])
			if str1 + str2 in self.ids_seen:
				raise DropItem("Duplicate item found: %s") %str1
			else:
				return item
		else:
			str1 = ''.join(item['address'])
			if str1 in self.ids_seen:
				raise DropItem("Duplicate item found: %s" % str1)
			else:
				self.ids_seen.add(str1)
				return item

class CSVPipeline(object):
	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline

	def spider_opened(self, spider):
		if spider.name in 'realestate':
			self.file = open('current_listing.csv', 'w+b')
		else:
			self.file = open('past_listing.csv', 'w+b')
		self.exporter = CsvItemExporter(self.file)
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
		self.file.close()

	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item