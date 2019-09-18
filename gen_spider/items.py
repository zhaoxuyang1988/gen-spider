# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GenSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    title = Field()  # 新闻标题
    content = Field()  # 正文
    summary = Field()  # 摘要
    pubtime = Field()   # 发布时间
    media = Field()
    srcLink = Field()
    sourceMeta = Field()
    origin = Field()
    createtime = Field()
    extra = Field()
    fetcherType = Field()
    scenes = Field()
