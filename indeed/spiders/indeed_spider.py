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
        for sel in response.xpath("//div[contains(@class, 'row')]")
            items = []
            jobs = sel.xpath('normalize-space(//a[contains(@data-tn-element, "jobTitle")])').extract()
            city = sel.xpath('normalize-space(//span[@class="location"])').extract()
            company = sel.xpath('normalize-space(//span[@class="company"]|//span[@itemprop = "hiringOrganization"])').extract()
            description = sel.xpath('normalize-space(//span[@class="summary"])').extract()
            for j, c, co, d in zip(jobs, city, company, description):
                position = IndeedItem()
                position['jobs'] = j.strip()
                position['city'] = c.strip()
                position['company'] = co.strip()
                position['description'] = d.strip()
                items.append(position)
            return items
