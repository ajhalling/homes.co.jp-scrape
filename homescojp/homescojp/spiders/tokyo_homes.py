# -*- coding: utf-8 -*-
import scrapy


target = ['https://www.homes.co.jp/chintai/tokyo/list/yh']

class TokyoHomesSpider(scrapy.Spider):
    name = 'tokyo_homes'
    allowed_domains = ['homes.co.jp']
    start_urls = target

    def parse(self, response):
        listings = response.xpath('//*[@class="mod-mergeBuilding--sale sbMansion ui-frame ui-frame-cacao-bar"]')
        
        for listing in listings:
            title = listing.xpath('.//*[@class="bukkenName"]/text()').extract_first()

        print(title)