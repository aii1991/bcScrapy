# -*- coding: utf-8 -*-

# Scrapy settings for bcScrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bcScrapy'

SPIDER_MODULES = ['bcScrapy.spiders']
NEWSPIDER_MODULE = 'bcScrapy.spiders'
ITEM_PIPELINES = {
    'bcScrapy.pipelines.FilterBcscrapyPipeline':1,
    'bcScrapy.pipelines.DBBcscrapyPipeline': 2
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bcScrapy (+http://www.yourdomain.com)'
