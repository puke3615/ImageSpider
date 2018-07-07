# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    thumbURL = scrapy.Field()
    middleURL = scrapy.Field()
    largeTnImageUrl = scrapy.Field()
    hasLarge = scrapy.Field()
    hoverURL = scrapy.Field()
    pageNum = scrapy.Field()
    objURL = scrapy.Field()
    fromURL = scrapy.Field()
    fromURLHost = scrapy.Field()
    currentIndex = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    type = scrapy.Field()
    filesize = scrapy.Field()
    bdSrcType = scrapy.Field()
    di = scrapy.Field()
    pi = scrapy.Field()
    partnerId = scrapy.Field()
    bdSetImgNum = scrapy.Field()
    bdImgnewsDate = scrapy.Field()
    fromPageTitle = scrapy.Field()
    bdSourceName = scrapy.Field()
    bdFromPageTitlePrefix = scrapy.Field()
    isAspDianjing = scrapy.Field()
    token = scrapy.Field()
    imgType = scrapy.Field()
    cs = scrapy.Field()
    os = scrapy.Field()
    source_type = scrapy.Field()
    adPicId = scrapy.Field()
