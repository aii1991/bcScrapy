# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from bcScrapy.models import ImageModel,DBSession,JokeTextModel

class FilterBcscrapyPipeline(object):
    def process_item(self, item, spider):
        if(spider["name"] == "bcimg"):
            url = item["url"].encode("utf-8")
            if("cover" in url):
                raise DropItem(item)
            return item
        return item


class DBBcscrapyPipeline(object):
    
    def open_spider(self,spider):
        self.session = DBSession();

    def process_item(self, item, spider):
        if(spider["name"] == "bcimg"):
            self.persistenceImg(item)
        if(spider["name"] == "jokeText"):
            self.persisitenceJokeText(item)
        return item

    def persistenceImg(self, item):
        title = ""
        desc = ""
        if(item.has_key("title")):
            title = item["title"].encode("utf-8")
        
        if(item.has_key("desc")):
            desc = item["desc"].encode("utf-8")
        
        imageModel = ImageModel(imgeId=item['imageId'],
            title=title,
            url=item['url'].encode("utf-8"),
            desc=desc)
        
        self.session.add(imageModel)
        self.session.commit()
    
    def persisitenceJokeText(self,item):
        jokeText = JokeTextModel(jokeId = item['jokeId'].encode("utf-8"),
            digest=item['digest'].encode("utf-8"),
            title=item['title'].encode("utf-8"))

        self.session.add(jokeText)
        self.session.commit()
    

    def close_spider(self,spider):
        self.session.close()