# -*- coding: utf-8 -*-
import scrapy


class AfishaSpider(scrapy.Spider):
    name = 'afisha'
    allowed_domains = ['afisha.ru']
    # start_urls = ['https://www.afisha.ru/']
    start_urls = ['https://www.afisha.ru/msk/cinema/cinema_list/']

    def parse(self, response):
        # a = response.selector.xpath('//*[@id="city-switcher_list"]/ul/li/a')
        # b = a.xpath('@href').extract()
        # c = response.selector.xpath('//*[@id="city-switcher_list"]/ul/li/a/text()').extract()
        # for index, link in enumerate(b):
        #     print('city_id - {0}, link -  {1}, city_name - {2}'.format(index, link, c[index]))

        # a = response.selector.xpath('//*[@id="background-ad-id__page"]/div[4]/article/section/ul/div/li/aside/div')
        a = response.selector.xpath('//*[@id="background-ad-id__page"]/div[4]/article/section/ul/div/li/aside/div/a/span/text()')
        print(a.extract())
        # print(a.xpath('@href').extract())

# scrapy crawl afisha
