from pathlib import Path

import scrapy

class PovertyHeadCountSpider(scrapy.Spider):
    name = "poverty_head_count"
    allowed_domains = ['www.worldbank.org']
    start_urls = ['https://data.worldbank.org/indicator/SI.POV.DDAY?end=2022&locations=1W-BR&start=1981']



    def parse_country(self, response):
        cases = response.xpath('.//div[@class="maincounter-number"]/span/text()').get()
        deaths = response.xpath('.//div[@class="maincounter-number"]/span/text()')[1].getall()
        recovered  = response.xpath('.//div[@class="maincounter-number"]/span/text()')[-1].getall()
        yield{
            'Cases' : cases,
            'Deaths' : deaths,
            'Recovered' : recovered,
        }