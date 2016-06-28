# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IndeedItem(scrapy.Item):
    company = scrapy.Field()
    city = scrapy.Field()
    State = scrapy.Field()
    jobs = scrapy.Field()
    job_title = scrapy.Field()
