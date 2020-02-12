# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituludemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgurl = scrapy.Field()  # 图片的地址
    imgname = scrapy.Field()  # 图片的编号
    imgtitle = scrapy.Field()  # 图片的所属文件夹

