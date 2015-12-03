# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealEstateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	address = scrapy.Field()
	postalCode = scrapy.Field()
	propertyType = scrapy.Field()
	price = scrapy.Field()
	bedrooms = scrapy.Field()
	bathrooms = scrapy.Field()
	car = scrapy.Field()
	descript = scrapy.Field()