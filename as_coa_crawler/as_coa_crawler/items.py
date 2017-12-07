# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AsCoaCrawlerItem(scrapy.Item):
    # title = scrapy.Field()
    # main_image = scrapy.Field()
    # image_caption = scrapy.Field()
    # posted_date = scrapy.Field()
    # description = scrapy.Field()
    # related = scrapy.Field()
    # url = scrapy.Field()

    eventImage = scrapy.Field() 
    organization = scrapy.Field()   #  (text format)
    title = scrapy.Field()    #(text format)
    description = scrapy.Field()   #(html format)
    eventWebsite = scrapy.Field()    # url/link - text format)
    street = scrapy.Field()      #(text format)
    city = scrapy.Field()       #(text format)
    state = scrapy.Field()        #(text format)
    zip = scrapy.Field()        #numeric format xxxxx)
    dateFrom = scrapy.Field()      #(REQUIRED FORMAT: dd/mm/yyyy)
    startTime = scrapy.Field()      #(REQUIRED FORMAT: hh:mm am/pm)
    In_group_id = scrapy.Field()
    ticketUrl = scrapy.Field()    #(url/link - text format)
