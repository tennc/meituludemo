# -*- coding: utf-8 -*-
import scrapy
from meituludemo.items import MeituludemoItem


class MeituluSpider(scrapy.Spider):
    name = 'meitulu'
    allowed_domains = ['meitulu.com']
    #start_urls = ['https://www.meitulu.com/item/']
    urlsnumber = 20988  # 最大页码数

    def parse(self, response):
        item = MeituludemoItem()
        imgurltemp = response.css('body  div.content  center  img::attr(src)').getall()
        title = response.css('body  div.width  div.weizhi  h1::text').get()
        for imgurl in imgurltemp:
            item['imgurl'] = [imgurl]
            item['imgname'] = str(imgurl).split("/")[-1]
            item['imgtitle'] = title
            yield item

        next_page = "https://www.meitulu.com/" + response.css('#pages  a::attr(href)')[-1].get()  # get()
        # self.log('url is %s' % next_page)
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def start_requests(self):
        start_urls = ['https://www.meitulu.com/item/']
        for i in range(800):
            url1 = start_urls[0] + str(i) + ".html"
            yield scrapy.Request(url=url1, callback=self.parse)
