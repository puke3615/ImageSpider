# coding=utf-8
from ImageSpider.spiders.BaiduImageSpider import SPIDER
from scrapy import cmdline

command = 'scrapy crawl %s' % SPIDER
cmdline.execute(command.split())
