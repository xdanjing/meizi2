# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
import json
import codecs
'''     image_poid = request.url.split('/')[5:8]
        image_file_po = ''.join(image_poid)
        return '%s/%s' % (image_file_po, image_file_name)'''


class meiziurlPipeline(object):
    def __init__(self):
        self.file = codecs.open('meiziurl.json', 'w', 'utf-8')

    def item_process(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line, '\n')
        yield item


class MeiziPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[5:]
        image_file_name = '_'.join(image_guid)
        return '%s' % image_file_name

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
