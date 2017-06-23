# -*- coding: utf-8 -*-
import scrapy
from bcScrapy.items import BcImgItem
import json
import time

class BcImgSpider(scrapy.Spider):
    maxPage = 1
    name = "bcimg"
    fn = 1
    
    wyUrl = "http://c.m.163.com/recommend/getChanListNews"
    wyParam = "channel=T1456112189138&size=10&offset={page}&fn={fn}&LastStdTime=0&passport=&devId=YJ7z2kAK9L8bRm2ahIovMEsbi0mBK%2B18s1foXHigDaHSI1Gc0ajkJNNSHvCb4oqH&lat=i4XPWLg5m4bykaWB4fOjiA%3D%3D&lon=DQ4cAxeuhTZomG4nd3PbQQ%3D%3D&version=24.1&net=wifi&ts=1498205284&sign=PFFgwa9oIBV78kUyX%2F2Z7iYfvGr4MgSnwVrdo4IkqBV48ErR02zJ6%2FKXOnxX046I&encryption=1&canal=baidu_cpd2_news&mac=racUMC0A9havm%2BHe6jH3YAvVdjgSXYDtwEDZ03eH1l8%3D&open=&openpath="
    allowed_domains = [
        "m.nvshens.com",
        "c.m.163.com"
    ]
    start_urls = [
        # "https://m.nvshens.com/"
    ]
    def __init__(self):
        self.initStarUrl()
        super(BcImgSpider,self).__init__()

    def parse(self,response):
        items = []
        if(self.allowed_domains[0] in response.url):
            self.parseZnns(response,items)

        if(self.allowed_domains[1] in response.url):
            self.parseWy(response,items)
            
        return items

    def __getitem__(self, name):
        return self.name

    
    def parseZnns(self,response,items):
        datas = response.xpath('//span[@class="ck-icon"]/img/@src')
        for data in datas:
            item = BcImgItem()
            item["url"] = data.extract()
            item["imageId"] = hash(item["url"])
            items.append(item)
        
    
    def parseWy(self,response,items):
        jsonData = json.loads(response.body)
        jsonArray = jsonData[u'\u7f8e\u5973']
        for data in jsonArray:
            item = BcImgItem()
            item["url"] = data["imgsrc"]
            item["imageId"] = hash(item["url"])
            item["title"] = data["title"]
            item["desc"] = data["digest"]
            items.append(item)

    def initStarUrl(self):
         for i in range(0,self.maxPage):
            start_url = self.wyUrl + "?" +self.wyParam.format(page=i)
            self.start_urls.append(start_url)
        