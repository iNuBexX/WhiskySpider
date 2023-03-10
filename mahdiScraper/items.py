# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def removecurrency(value):
    return value.replace('₴','').strip()# do note that this symbol is that of the ukrainian currency Hryvnia

class MahdiscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags),output_processor= TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags,removecurrency),output_processor= TakeFirst())
    link = scrapy.Field()
    pass
