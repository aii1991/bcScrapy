# -*- coding: utf-8 -*-
import scrapy
from bcScrapy.items import BcJokeTextItem
import json

class BcJokeTextSpider(scrapy.Spider):
    name = "jokeText"
    maxPage = 30
    allowed_domains = ["c.m.163.com"]
    url = "http://c.m.163.com/recommend/getChanListNews"
    param = "channel=T1419316284722&size=40&offset={page}&fn=4&LastStdTime=0&passport=&devId=YJ7z2kAK9L8bRm2ahIovMEsbi0mBK%2B18s1foXHigDaHSI1Gc0ajkJNNSHvCb4oqH&lat=OVxfr0O22mHDkgZmFVZ2Ng%3D%3D&lon=sfehuqPVBNUXZpHUuHh%2BAQ%3D%3D&version=24.1&net=wifi&ts=1498186406&sign=6GoyJWGMlGWuA2kkWbACM6HwseAliBc1g6lZ8Dx5L7d48ErR02zJ6%2FKXOnxX046I&encryption=1&canal=baidu_cpd2_news&mac=racUMC0A9havm%2BHe6jH3YAvVdjgSXYDtwEDZ03eH1l8%3D&open=&openpath="
    start_urls = []
    def __init__(self):
        self.initStarUrl()
        super(BcJokeTextSpider,self).__init__()

    def parse(self,response):
        print("url=====>"+response.url)
        items = []
        jsonData = json.loads(response.body,encoding="utf-8")
        jokeArray = jsonData[u'\u6bb5\u5b50']
        for jokeItem in jokeArray:
            item = BcJokeTextItem()
            item["digest"] = jokeItem["digest"]
            item["jokeId"] = jokeItem["docid"]
            item["title"] = jokeItem["title"]
            items.append(item)
        return items
        # yield scrapy.Request(url, callback=self.parse_dir_contents)  
    
    def __getitem__(self, name):
        return self.name

    
    def initStarUrl(self):
         for i in range(0,self.maxPage):
            start_url = self.url + "?" +self.param.format(page=i)
            self.start_urls.append(start_url)
        