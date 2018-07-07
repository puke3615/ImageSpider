# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

from scrapy import Request
import json
import os

KEYS = ['fromPageTitle', 'thumbURL', 'objURL']

SAVE_DIR = 'data'
path = lambda sub_dir: os.path.join(SAVE_DIR, sub_dir)
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


class EncodePipeline(object):
    def process_item(self, item, spider):
        encode = lambda s: s.encode('utf-8') if isinstance(s, unicode) else s
        return dict((encode(k), encode(v)) for k, v in item.items() if KEYS.__contains__(k))


class JsonPipeline(object):
    data = []

    def process_item(self, item, spider):
        self.data.append(item)
        return item

    def close_spider(self, spider):
        with open(path('data.json'), 'w') as f:
            json.dump(self.data, f, ensure_ascii=False)


class TextPipeline(object):
    data = []

    def process_item(self, item, spider):
        offset = 1
        max_length = max([len(key) for key in item.keys()])
        key_format = lambda key: key + ' ' * (max_length - len(key) + offset)
        item_str = ''.join(['%s: %s\n' % (key_format(k), v) for k, v in item.items()])
        self.data.append(item_str)
        return item

    def close_spider(self, spider):
        with open(path('data.text'), 'w') as f:
            f.write('\n'.join(self.data))
        print('*' * 200)
        print('Total % image' % len(self.data))
        print('*' * 200)


class MarkdownPipeline(object):
    data = []

    def process_item(self, item, spider):
        item_str = '[%s](%s)\n![](%s)\n' % (item['fromPageTitle'], item['objURL'], item['thumbURL'])
        self.data.append(item_str)
        return item

    def close_spider(self, spider):
        with open(path('data.md'), 'w') as f:
            f.write('\n'.join(self.data))


class DownLoadImgPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        folder = info.spider.keyword
        filename = request.url.split('/')[-1]
        file_path = os.path.join(folder, filename)
        return file_path

    def get_media_requests(self, item, info):
        yield Request(item['objURL'])

    def item_completed(self, results, item, info):
        if isinstance(item, dict) or self.images_result_field in item.fields:
            item[self.images_result_field] = [x for ok, x in results if ok]
        return item
