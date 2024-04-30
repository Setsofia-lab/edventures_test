from pathlib import Path

import scrapy

class InternetUsageSpider(scrapy.Spider):
    name = "internet_usage_spider"
    allowed_domains = ['www.worldbank.org']
    start_urls = ['https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W-BR']



    def parse(self, response):
        gdp_stats = response.xpath('.//table/tbody/tr')
        for stat in gdp_stats:
            countries = stat.xpath('.//th/a/text()').get()
            nationaldebt = stat.xpath('.//td[1]/text()').get()
            gdp_percentage = stat.xpath('.//td[2]/text()').get()
            debtpercapital = stat.xpath('.//td[3]/text()').get()
            year = stat.xpath('.//td[4]/text()').get()
            yield {
                'Countries' : countries,
                'National Debt' : nationaldebt,
                'Percentage of GDP' : gdp_percentage,
                'Debt per Capita' : debtpercapital,
                'Data Year' : year
            }