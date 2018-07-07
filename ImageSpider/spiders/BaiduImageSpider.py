# coding=utf-8
from ImageSpider.items import ImageItem
from scrapy import Request
import scrapy
import json
import sys
import re

IMAGES_STORE = '/Users/puke/Documents/spider'  # 保存图片的文件夹
KEYWORDS = ['金毛', '边牧']  # 搜索关键词
PAGE_LIMIT = 1  # 最大页数限制(0表示不限制)

SPIDER = 'image'
URL = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d'

arg = sys.argv
keywords = KEYWORDS if len(arg) < 2 else arg[1].split('-')


def get_url(keyword, page=0):
    return URL % (keyword, page * 20)


class BaiduImageSpider(scrapy.Spider):
    page = 0
    index = 0
    keyword = keywords[index]

    name = SPIDER
    start_urls = [get_url(keyword)]

    def start_next(self):
        self.index += 1
        if self.index < len(keywords):
            self.keyword = keywords[self.index]
            self.page = 0
            url = get_url(self.keyword, self.page)
            return Request(url)

    def parse(self, response):
        if response.status != 200:
            # yield self.start_next()
            request = self.start_next()
            if request:
                yield request
            else:
                return
        text = response.text
        pattern = r"(?<=flip\.setData\('imgData',\s).*(?=\);)"
        match = re.search(pattern, text)
        if match:
            json_data = None
            text = match.group()
            text = text.replace("\\'", "")
            try:
                json_data = json.loads(text)
            except Exception as e:
                print(e)

            if json_data:
                data = [image for image in json_data['data'] if image]
                for image in data:
                    image.pop('is')
                    yield ImageItem(**image)

        self.page += 1
        if PAGE_LIMIT and self.page >= PAGE_LIMIT:
            request = self.start_next()
            if request:
                yield request
            else:
                return
        yield Request(get_url(self.keyword, self.page))
