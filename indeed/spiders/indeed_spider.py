import scrapy
from indeed.items import IndeedItem


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ['www.indeed.com']
    start_urls = [
        'http://www.indeed.com/jobs?as_and=&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=50&l=19103&fromage=30&limit=10&sort=&psf=advsrch'
        ]

    def parse(self, response):

        for sel in response.xpath("//div[contains(@class, 'row ')]"):
            position = IndeedItem()
            position['jobs'] = sel.xpath('//a[contains(@data-tn-element, "jobTitle")]/text()').extract()
            position['city'] = sel.xpath('//span[@class="location"]/text()').extract()
            position['company'] = sel.xpath('//span[@class="company"]/text()').extract()

            return position
