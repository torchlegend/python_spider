# -*- coding: utf-8 -*-
import scrapy


class MyspiderSpider(scrapy.Spider):
    name = 'cpuSpider'
    start_urls = ['https://rank.kkj.cn/dcpu.shtml']

    def parse(self, response):
        for each in response.xpath('//*[@id="pcCpuList"]/tr'):
            cpu = {  # 'name': each.xpath('./td[3]/ul/li[1]').extract_first(),
                'name': each.css('li.model1::text').extract_first(),
                'time': each.css('li.times1::text').extract_first(),
                'score': each.css('li.mark1::text').extract_first()
            }
            yield cpu

