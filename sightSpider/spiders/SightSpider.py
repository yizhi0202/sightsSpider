
from __future__ import absolute_import
import scrapy
from ..items import SightspiderItem


class SightspiderSpider(scrapy.Spider):
    name = 'SightSpider'
    allowed_domains = ['piao.qunar.com']
    start_urls = ['https://piao.qunar.com/ticket/list.htm?keyword=北京']

    def parse(self, response):
        sight_items = response.css('#search-list .sight_item')
        for sight_item in sight_items:
            item = SightspiderItem()
            item['sightLocation'] = sight_item.css(
                '::attr(data-address)').extract_first()
            item['sightName'] = sight_item.css(
                '::attr(data-sight-name)').extract_first()
            item['coordinate'] = sight_item.css(
                '::attr(data-point)').extract_first()
            item['photoUrl'] = sight_item.css(
                '::attr(data-sight-img-u-r-l)').extract_first()
            item['intro'] = sight_item.css(
                '.intro.color999::text').extract_first()
            yield item

        next_url = response.css('.next::attr(href)').extract_first()
        if next_url:
            next_url = next_url.split('&')[-1]
            next_url = "https://piao.qunar.com/ticket/list.htm?keyword=北京&" + next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
        pass
