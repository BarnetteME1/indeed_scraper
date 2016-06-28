import scrapy
from indeed.items import IndeedItem


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ['www.indeed.com']
    start_urls = [
        'http://www.indeed.com/jobs?q=&l=19103&radius=50'
        ]

    def parse(self, response):
        ij = scrapy.Selector(response)
        jobs = ij.xpath("//div[@class='row  result' or @class-'row sjlast result']")
        openings = []

        for job in jobs:
            position = IndeedItem()
            position['jobs'] = jobs.xpath('a[@target="_blank"]/text()').extract()
            openings.append(position)
        print("Openings: ", openings)
