from pathlib import Path

import scrapy

#This spider just crawls the link provided and extracts the whole website
#It does not extract specific data it just extracts the whole website and saves in a local file

class BrazilDataSpider(scrapy.Spider): 
    name = "brazildata" 
    start_urls = [
        "https://data.worldbank.org/indicator/SI.POV.DDAY?locations=1W-BR",
        "https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W-BR",
        "https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=1W-BR",
    ]
        

    def parse(self, response):
        page = response.url.split("/")
        filename = f"brazildata-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")