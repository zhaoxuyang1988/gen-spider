# -*-coding:utf-8 -*-

import scrapy

from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import CrawlSpider



        
class GenSpider(CrawlSpider):

    name = "gen_spider"

    def __init__(self,  *a, **kw):
        self.rules = (
            Rule(LinkExtractor(allow="china5e.com/news/news-.*?\\d+.html"), callback="parse_article"),
            )
        self.start_urls = ["https://www.china5e.com/power/coal-fire/"]
        super(GenSpider, self).__init__(*a, **kw)
    

    
    def get_values(self):
        return  {'author': '周健', 'webName': '中国能源报', 'channelName': '火电', 'channelId': 6285, 'createDate': '2019-09-06 15:27:45', 'yamlFileName': 'china5e_huodian.yaml', 'webUrl': 'https://www.china5e.com', 'channelUrl': 'https://www.china5e.com/power/coal-fire/', 'spider': {'clsPath': 'templateSpider', 'settings': {'DOWNLOAD_DELAY': 1, 'RETRY_TIME': 1, 'DOWNLOAD_TIMEOUT': 30, 'PROXY': False}, '说明': '配置指定的spider名称、DOWNLOAD_DELAY参数为下载延迟参数、决定采集频率; DOWNLOAD_TIMEOUT为下载超时参数，决定一次请求的最大等待时间; RETRY_TIME为下载失败时重试的总次数'}, 'rules': {'allow': 'china5e.com/news/news-.*?\\d+.html', 'deny': 'video', 'restrict_xpaths': None}, 'parser': {'request': 'get', 'settings': {'header': None, 'cookie': None, 'formData': None, 'body': None, 'useSelenium': False}, 'pubdate': {'xpath': './/div[@id="articleBox"]/div[@class="showtitle"]', 're': '\\d{2,4}-\\d{1,2}-\\d{1,2}\\s\\d{1,2}\\:\\d{1,2}'}, 'title': {'xpath': './/div[@id="articleBox"]/div[@class="showtitle"]//h1/text()', 're': '.+'}, 'origin': {'xpath': './/div[@class="showtitle"]/div[@class="showtitinfo"]/text()', 're': '.+'}, 'content': {'xpath': './/div[@id="articleBox"]/div[@id="showcontent"]/div', 're': '[\\s\\S]+', 'kill_xpath': '//div[@class="killxpath"]'}, 'isUrl': {'xpath': None, 're': None, 'baseUrl': 'www.xxxxx./ss + xpath'}, 'parse': {'request': 'post', 'settings': {'header': None, 'cookie': None, 'formData': None, 'body': None, 'useSelenium': True}, 'origin': {'xpath': './/div[@class="showtitle"]/div[@class="showtitinfo"]/text()', 're': '.+'}, 'content': {'xpath': './/div[@id="articleBox"]/div[@id="showcontent"]/div', 're': '[\\s\\S]+', 'kill_xpath': '//div[@class="killxpath"]'}}}}

    def parse_article(self, response):
        print(response.url)
        pass
