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
    rules = (
    Rule (LinkExtractor(allow_domains=()), callback="parse_jobs"),
    Rule (LinkExtractor(allow_domains=(), restrict_xpaths=('//span[@class="np"]')), follow=True), )


    def parse_jobs(self, response):
        for sel in response.xpath("//div[contains(@class, 'row ')]"):
            items = []
            jobs = sel.xpath('//a[contains(@data-tn-element, "jobTitle")]/text()').extract()
            city = sel.xpath('//span[@class="location"]/text()').extract()
            if sel.xpath('//span[@class="company"]/text()').extract() != "":
                company = sel.xpath('//span[@class="company"]/text()').extract()
            elif sel.xpath('//span[contains(@itemprop, "name")]/text()').extract() != "":
                company = sel.xpath('//span[contains(@itemprop, "name")]/text()').extract()
            elif sel.xpath('//a[contains(@data-tn-element, "companyName")]/text()').extract() != "":
                company = sel.xpath('//a[contains(@data-tn-element, "companyName")]/text()').extract()
            elif sel.xpath('//a[contains(@target, "blank"])/text()').extract() != "":
                company = sel.xpath('//a[contains(@target, "blank"])/text()').extract()
            description = sel.xpath('//span[@class="summary"]/text()').extract()
            for j, c, co, d in zip(jobs, city, company, description):
                position = IndeedItem()
                position['jobs'] = j.strip()
                position['city'] = c.strip()
                position['company'] = co.strip()
                position['description'] = d.strip()
                items.append(position)
            return items
