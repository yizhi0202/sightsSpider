# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SightspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sightLocation = scrapy.Field()
    sightName = scrapy.Field()
    coordinate = scrapy.Field()
    photoUrl = scrapy.Field()
    intro = scrapy.Field()
    pass
