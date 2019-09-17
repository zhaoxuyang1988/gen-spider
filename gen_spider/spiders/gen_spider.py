# -*-coding:utf-8 -*-

import scrapy
from gerapy.spiders.crawl import CrawlSpider



class GenSpider(CrawlSpider):
    
    name = "gen_spider"
    
    def __init__(self, **kwargs):
        
        # -----
        super(GenSpider, self).__init__(kwargs)