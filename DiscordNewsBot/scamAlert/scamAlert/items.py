# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ScamNewsItem(scrapy.Item):
   author = scrapy.Field()
   content = scrapy.Field()
   title = scrapy.Field()
   url = scrapy.Field()
   time = scrapy.Field()
   type = scrapy.Field()
   isPosted = scrapy.Field()
   isValid = scrapy.Field()