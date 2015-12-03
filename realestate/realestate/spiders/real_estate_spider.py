import scrapy

# from realestate.items import RealEstateItem

# class RealEstateSpider(scrapy.Spider):
	# name = "realestate"
	# allowed_domains = ["realestate.com.au"]
	# start_urls = [
		# "http://www.realestate.com.au/property-apartment-nsw-sydney-121365778",
	# ]
	
	# def parse_dir_contents(self, response):
		# item = RealEstateItem()
		# item['address'] = response.xpath('//div[4]/div/div[1]/div[3]/h3/text()').extract()
		# item['postalAddress']= response.xpath('//div[4]/div/div[1]/div[1]/div[1]/h1/span[4]/text()').extract()
		# item['propertyType'] = response.xpath('//div[4]/div/div[1]/div[1]/div[3]/ul/li[2]/span/text()').extract()
		# item['bedrooms'] = response.xpath('//div[4]/div/div[1]/div[6]/div[1]/div/ul[1]/li[3]/span/text()').extract()
		# item['bathrooms'] = response.xpath('//div[4]/div/div[1]/div[6]/div[1]/div/ul[1]/li[4]/span/text()').extract()
		# item['car'] = response.xpath('//body/div[4]/div/div[1]/div[6]/div[2]/div/ul/li[2]/span/text()').extract()
		# item['descript'] = response.xpath('//div[4]/div/div[1]/div[3]/p[2]/text()').extract()
		# yield item
		
class RealEstateSpider(scrapy.Spider):
	name = "realestate"
	allowed_domains = ["www.realestate.com.au"]
	start_urls = [
        "http://www.realestate.com.au/property-apartment-nsw-sydney-121365778",
	]
	
	def parse(self, response):
		item = RealEstateItem()
		item['address'] = response.xpath('//div[4]/div/div[1]/div[3]/h3/text()').extract()
		item['postalAddress']= response.xpath('//div[4]/div/div[1]/div[1]/div[1]/h1/span[4]/text()').extract()
		item['propertyType'] = response.xpath('//div[4]/div/div[1]/div[1]/div[3]/ul/li[2]/span/text()').extract()
		item['price'] = response.xpath('//div[4]/div/div[1]/div[1]/div[3]/ul/li[1]/p/text()').extract()
		item['bedrooms'] = response.xpath('//div[4]/div/div[1]/div[6]/div[1]/div/ul[1]/li[3]/span/text()').extract()
		item['bathrooms'] = response.xpath('//div[4]/div/div[1]/div[6]/div[1]/div/ul[1]/li[4]/span/text()').extract()
		item['car'] = response.xpath('//div[4]/div/div[1]/div[6]/div[2]/div/ul/li[2]/span/text()').extract()
		item['descript'] = response.xpath('//div[4]/div/div[1]/div[3]/p[2]/text()').extract()
		yield item