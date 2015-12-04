import scrapy

from realestate.items import RealEstateItem

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
        "http://www.realestate.com.au/buy/in-sydney%2c+nsw+2000%3b/list-1",
	]
	
	def parse(self, response):
		for href in response.css("a.name::attr('href')"): #start with the main page
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback = self.parse_details)
			
		nextUrl = response.css("li.nextLink > a::attr('href')").extract()
		if nextUrl: #if there is a next link go to it
			yield scrapy.Request(response.urljoin(nextUrl[0]), self.parse)

	def parse_details(self, response):
		item = RealEstateItem()
		item['address'] = response.css('h3[class="address"]::text').extract()
		item['postalCode']= response.css('span[itemprop="postalCode"]::text').extract()
		item['propertyType'] = response.css('span[class="propertyType"]::text').extract()
		item['price'] = response.css('li.price>p.priceText::text').extract()
		item['bedrooms'] = response.css('.rui-icon-bed+dd::text').extract()
		item['bathrooms'] = response.css('.rui-icon-bath+dd::text').extract()
		item['car'] = response.css('.rui-icon-car+dd::text').extract()
		item['descript'] = response.css('p[class="body"]::text').extract()
		yield item