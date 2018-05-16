# -*- coding: utf-8 -*-
import scrapy


class AfishaSpider(scrapy.Spider):
    name = 'afisha'
    allowed_domains = ['afisha.ru']
    start_urls = ['https://www.afisha.ru//']

    def parse(self, response):
        a = response.selector.xpath('//*[@id="city-switcher_list"]/ul/li/a')
        b = a.xpath('@href').extract()
        c = response.selector.xpath('//*[@id="city-switcher_list"]/ul/li/a/text()').extract()
        for index, link in enumerate(b):
            print('city_id - {0}, link -  {1}, city_name - {2}'.format(index, link, c[index]))

# scrapy crawl afisha
