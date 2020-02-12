# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MeituludemoImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['imgurl']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = item['imgtitle']
        return item


class MeituludemoPipeline(object):
    def process_item(self, item, spider):
        return item


class DownImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['imgurl']:
            yield scrapy.Request(image_url,
                                 meta={'item': item, 'name': item['imgname'],
                                       'patch': item['imgtitle']})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过上面的meta传递过来item
        index = request.meta['index']
        image_paths = request.meta['patch']
        name = request.meta['name']
        down_file_name = u'full/{0}/{1}'.format(image_paths, name)
        return down_file_name
