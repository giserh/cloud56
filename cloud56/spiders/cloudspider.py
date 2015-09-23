# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from cloud56.items import Cloud56Item


class CloudspiderSpider(scrapy.Spider):
    name = "cloudspider"
    allowed_domains = ["cloud56.net"]
    download_delay = 0.1
    start_urls = (
        'http://www.cloud56.net/Transport/page1',
    )

    def parse(self, response):
        sel = Selector(response)
        links = sel.xpath('//*[@id="xx"]//table//tr/td/a/@href').extract()
        # print links
        for link in links:
            infourl = 'http://www.cloud56.net' + \
                (link.replace('\t', '').replace('\n', '').replace(' ', ''))
            yield Request(infourl, self.parse_info, headers={'Upgrade-Insecure-Requests': '1', 'Host': 'www.cloud56.net'})
        for i in range(73):
            nexturl = 'http://www.cloud56.net/Transport/page' + str(i + 2)
            yield Request(nexturl, self.parse)

    def parse_info(self, response):
        item = Cloud56Item()
        sel = Selector(response)
        print response.request.headers.get('Referer', None)
        # print response.body
        infos = sel.xpath(
            '//*[@class="data"]/table//tr/td[2]/text()').extract()
        try:
            item['plateno'] = infos[0].strip()
            item['carlength'] = infos[1].strip()
            item['mount'] = infos[2].strip()
            item['area'] = infos[3].strip()
            item['trucktype'] = infos[4].strip()
            item['truckinfo'] = infos[5].strip()
            item['contact'] = infos[6].strip()
            item['tele'] = infos[7].strip()
            item['phone'] = infos[8].strip()
            item['driverlicence'] = infos[9].strip()
            item['icid'] = infos[10].strip()
        except Exception, e:
            raise e
        return item
