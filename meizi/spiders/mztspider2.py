# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from meizi.items import MeiziItem


class MztspiderSpider(CrawlSpider):
    name = 'mztspider2'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://www.meizitu.com/a/list_1_%s.html' % urlnum for urlnum in range(1, 92)]

    rules = (
        Rule(LinkExtractor(allow='meizitu.com/a', restrict_xpaths='//ul[@class="wp-list clearfix"]/li/div/div/a'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        sel = Selector(response)
        srcs = sel.xpath('//div[@id="picture"]/p/img/@src').extract()
        item = MeiziItem()
        item['image_urls'] = srcs
        yield item
