import scrapy
from indeed.items import IndeedItem


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    allowed_domains = ['www.indeed.com']
    start_urls = [
        'http://www.indeed.com/jobs?as_and=&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=50&l=19103&fromage=30&limit=10&sort=&psf=advsrch'
        ]

    def parse(self, response):
        ij = scrapy.Selector(response)
        jobs = ij.xpath("//div[contains(@class, ' row ']")
        job_list = jobs.xpath('//a[@class="jobTitle"]/text()').extract()
        city = jobs.xpath('//span[@class="location"]/text()').extract()
        company = jobs.xpath('//span[@class="company"]/text()').extract()
        openings = []
        count = 0
        for job in job_list:
            position = IndeedItem()
            position['jobs'] = job
            position['city'] = city[count]
            position['company'] = company[count]
            openings.append(position)
            count += 1
        return openings
