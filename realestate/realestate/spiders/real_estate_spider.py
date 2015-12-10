import scrapy

from realestate.items import RealEstateItem

class RealEstateSpider(scrapy.Spider):
	name = "realestate"
	allowed_domains = ["www.realestate.com.au"]
	#open the postcode file
	f = open("postCode.txt")
	start_urls = [
		"http://www.realestate.com.au/buy/in-nsw+" + n.rstrip()+ "/list-1?includeSurrounding=false" for n in f.readlines()
	]
	f.close()
	
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
		item['sold_date']= []
		yield item