# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cloud56Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    plateno = scrapy.Field()
    carlength = scrapy.Field()
    mount = scrapy.Field()
    area = scrapy.Field()
    trucktype = scrapy.Field()
    truckinfo = scrapy.Field()
    contact = scrapy.Field()
    tele = scrapy.Field()
    phone = scrapy.Field()
    driverlicence = scrapy.Field()
    icid = scrapy.Field()
    pass
