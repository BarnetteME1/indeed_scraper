import scrapy
from scrapy.linkextractors import LinkExtractor
from indeed.items import IndeedItem

class IndeedSpider(scrapy.Spider):
    name = "indeedtwo"
    allowed_domains = ['www.indeed.com']
    start_urls = [
        'http://www.indeed.com/jobs?as_and=&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=50&l=19103&fromage=30&limit=10&sort=&psf=advsrch'
        ]

    def parse(self, response):
        sel = response.xpath("//div[contains(@class, 'row ')]")
        position = IndeedItem()
        position['jobs'] = j.strip()
        position['city'] = c.strip()
        position['company'] = co.strip()
        return position
