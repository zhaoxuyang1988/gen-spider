# -*- coding:utf-8 -*-
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


if __name__ == "__main__":
    
    c = CrawlerProcess(get_project_settings())
    c.crawl("gen_spider")
    c.start()