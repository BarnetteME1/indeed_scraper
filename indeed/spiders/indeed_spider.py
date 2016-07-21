import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from indeed.items import IndeedItem


class IndeedSpider(CrawlSpider):
    name = "indeed"
    allowed_domains = ['www.indeed.com']
    start_urls = [
        'http://www.indeed.com/jobs?as_and=&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=50&l=19103&fromage=30&limit=10&sort=&psf=advsrch'
        ]
    rules = (Rule(LinkExtractor(allow_domains=()), callback="parse_jobs"), )


    def parse_jobs(self, response):
        for sel in response.xpath("//div[contains(@class, 'row ')]"):
            #position = IndeedItem()
            items = []
            jobs = sel.xpath('//a[contains(@data-tn-element, "jobTitle")]/text()').extract()
            city = sel.xpath('//span[@class="location"]/text()').extract()
            company = sel.xpath('//span[@class="company"]/text()').extract()
            for j, c, co in zip(jobs, city, company):
                position = IndeedItem()
                position['jobs'] = j.strip()
                position['city'] = c.strip()
                position['company'] = co.strip()
                items.append(position)
            return items
