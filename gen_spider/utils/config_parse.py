# -*- coding:utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from spiders.general_crawl_spider import GenRule

class ConfigParser(object):
    
    def __init__(self, config_data):
        self.ori_config = config_data

    @property
    def start_urls(self):
        return [self.ori_config.get("channelUrl", None)]

    @property
    def custom_settings(self):
        return self.ori_config.get("spider", {}).get("settings", None)
    
    @property
    def allowed_domains(self):
        return ""

    @property
    def rules(self):
        
        return (GenRule(LinkExtractor(**self.ori_config.get("rules", {})), callback="parse_article", request_parm=self.request_param),)
        #return (Rule(tuple([LinkExtractor(extra) for extra in self.ori_config.get("rules", [])]), callback="parse_article"))
    @property
    def request_param(self):
        # request_parm = {"method":'POST', "headers":None, 
        #                 "body":None, "cookies":None, "meta":None, 
        #                  "encoding":'utf-8', "priority":0,
        #                  "dont_filter":False, "errback":None, "flags":None}
        
        maps = ["method", "headers", "body", "cookies", "meta", 
        "encoding", "priority", "dont_filter", "errback", "flags"]
        ori_param = {}
        
        for k,v in self.ori_config.get("parser", {}).get("settings", {}).items():
            if k not in maps:
                continue
            ori_param[k] = v
        return ori_param
            
    # need parse settings

if __name__ == "__main__":
    config =  {'author': '周健', 'webName': '中国能源报', 'channelName': '火电', 'channelId': 6285, 'createDate': '2019-09-06 15:27:45', 'yamlFileName': 'china5e_huodian.yaml', 'webUrl': 'https://www.china5e.com', 'channelUrl': 'https://www.china5e.com/power/coal-fire/', 'spider': {'clsPath': 'templateSpider', 'settings': {'DOWNLOAD_DELAY': 1, 'RETRY_TIME': 1, 'DOWNLOAD_TIMEOUT': 30, 'PROXY': False}, '说明': '配置指定的spider名称、DOWNLOAD_DELAY参数为下载延迟参数、决定采集频率; DOWNLOAD_TIMEOUT为下载超时参数，决定一次请求的最大等待时间; RETRY_TIME为下载失败时重试的总次数'}, 'rules': {'allow': 'china5e.com/news/news-.*?\\d+.html', 'deny': 'video', 'restrict_xpaths': None}, 'parser': {'request': 'get', 'settings': {'header': None, 'cookie': None, 'formData': None, 'body': None, 'useSelenium': False}, 'pubdate': {'xpath': './/div[@id="articleBox"]/div[@class="showtitle"]', 're': '\\d{2,4}-\\d{1,2}-\\d{1,2}\\s\\d{1,2}\\:\\d{1,2}'}, 'title': {'xpath': './/div[@id="articleBox"]/div[@class="showtitle"]//h1/text()', 're': '.+'}, 'origin': {'xpath': './/div[@class="showtitle"]/div[@class="showtitinfo"]/text()', 're': '.+'}, 'content': {'xpath': './/div[@id="articleBox"]/div[@id="showcontent"]/div', 're': '[\\s\\S]+', 'kill_xpath': '//div[@class="killxpath"]'}, 'isUrl': {'xpath': None, 're': None, 'baseUrl': 'www.xxxxx./ss + xpath'}, 'parse': {'request': 'post', 'settings': {'header': None, 'cookie': None, 'formData': None, 'body': None, 'useSelenium': True}, 'origin': {'xpath': './/div[@class="showtitle"]/div[@class="showtitinfo"]/text()', 're': '.+'}, 'content': {'xpath': './/div[@id="articleBox"]/div[@id="showcontent"]/div', 're': '[\\s\\S]+', 'kill_xpath': '//div[@class="killxpath"]'}}}}
    c = ConfigParser(config)
    print(c.start_urls)
    print(c.rules)