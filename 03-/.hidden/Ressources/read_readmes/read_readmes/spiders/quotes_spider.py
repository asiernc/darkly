from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	
	def start_requests(self):
		urls = [
			"https://docs.scrapy.org/en/latest/intro/tutorial.html",
			"https://docs.scrapy.org/en/latest/topics/debug.html"
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
	
	def parse(self, response):
		page = response.url.split("/")[-1].replace(".html", "")
		title = response.css('title::text').get()
		headings = response.css('h1::text, h2::text').getall()
		paragraphs = response.css('p::text').getall()[:3]
		
		yield {
			'url': response.url,
			'page': page,
			'title': title,
			'headings': headings,
			'paragraphs': paragraphs
		}