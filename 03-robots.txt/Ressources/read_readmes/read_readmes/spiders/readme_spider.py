import scrapy
import json
from scrapy import signals

class ReadmeSpider(scrapy.Spider):
	name = 'findFlag'
	start_url = [
		"http://x.x.x.x/.hidden"
	]
	readme_data = {}
	
	def from_crawler(cls, crawler, *args, **kwargs):
		spider = super().from_crawler(crawler, *args, **kwargs)
		crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
		return spider

	def spider_closed(self, spider):
		with open("result.log", 'w') as f:
			json.dump(self.readme_data, f, indent=2)
		self.logger.info("Se guardaron los datos en result.log")

	def parse(self, response):
		links = response.css('a::attr(href)').getall()
		for href in links:
			if href == '../':
				continue
			if href == 'README':
				yield response.follow(href, callback=self.parse_readme)
			else:
				yield response.follow(href, callback=self.parse)
	
	def parse_readme(self, response):
		content = response.body
		self.readme_data[1] = content