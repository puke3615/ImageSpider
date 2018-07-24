# coding=utf-8
from ImageSpider.items import ImageItem
from scrapy import Request
import argparse
import scrapy
import json
import re
import os

DEFAULT_KEYWORDS = ['金毛', '边牧']  # 搜索关键词
DEFAULT_IMAGES_STORE = '/Users/puke/Documents/spider'  # 保存图片的文件夹
DEFAULT_PAGE_LIMIT = 1  # 最大页数限制(0表示不限制)

SPIDER = 'image'
URL = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%s&pn=%d'

parser = argparse.ArgumentParser('参数协议')
parser.add_argument('--keywords', type=str, help='搜索关键词')
parser.add_argument('--folder', type=str, default=DEFAULT_IMAGES_STORE, help='图片保存目录')
parser.add_argument('--limit', type=int, default=DEFAULT_PAGE_LIMIT, help='图片页数显示')
args = parser.parse_args()

keywords = args.keywords.split('-')
folder = args.folder
limit = max(args.limit, 0)

if not os.path.exists(folder):
    os.makedirs(folder)

if raw_input('是否打开该文件夹: %s? (y/n)\n' % folder) == 'y':
    os.system('open %s' % folder)

description = '>>> 爬虫配置 <<<\n' \
              '搜索关键词: %s\n' \
              '图片保存目录: %s\n' \
              '爬取的图片页数(0表示爬取所有图片, 默认值为1): %d\n' \
              '是否开始爬取？(y/n)\n' \
              % (', '.join(keywords), os.path.abspath(folder), limit)

if raw_input(description) != 'y':
    exit(0)


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
        if self.index > len(keywords) - 1:
            return None
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
                if data:
                    for image in data:
                        image.pop('is')
                        yield ImageItem(**image)
                else:
                    request = self.start_next()
                    if request:
                        yield request
                    else:
                        return

        self.page += 1
        if limit and self.page >= limit:
            request = self.start_next()
            if request:
                yield request
            else:
                return
        yield Request(get_url(self.keyword, self.page))
