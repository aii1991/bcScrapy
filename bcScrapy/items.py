# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BcImgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imageId = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    desc = scrapy.Field()


class BcJokeTextItem(scrapy.Item):
    digest = scrapy.Field()
    jokeId = scrapy.Field()
    title = scrapy.Field()

