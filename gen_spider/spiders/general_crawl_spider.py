# -*- coding:utf-8 -*-

from scrapy.spiders.crawl import CrawlSpider

from scrapy.spiders import Rule

from scrapy.http import Request, HtmlResponse
from scrapy.utils.spider import iterate_spider_output
from scrapy.spiders import Spider


class GenRule(Rule):

    def __init__(self,  *a, **kw):

        self.request_parm = kw.pop("request_parm", {})
        super(GenRule, self).__init__(*a, **kw)

class GenCrawlSpider(CrawlSpider):
    
    
    def _build_request(self, rule, link,
                       method='GET', headers=None, body=None,
                 cookies=None, meta=None, encoding='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None):
        # ----- 可能需要指定函数  form request 等
        r = Request(link.url, self._response_downloaded, method, headers, body,
                 cookies, meta, encoding, priority,
                 dont_filter, errback, flags)

        r.meta.update(rule=rule, link_text=link.text)
        return r

    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)

                r = self._build_request(n, link, **rule.request_parm)
                yield rule.process_request(r)
