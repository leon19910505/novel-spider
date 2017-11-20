
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class SpiderPipeline(object):
    def __init__(self):
        connection = MongoClient(
            'localhost',
            27017
        )
        self.db = connection['spider']

    def process_item(self, item, spider):
        class_name =item.__class__.__name__

        if class_name == 'BookItem':

            book = self.db.book
            book.insert(dict(item))
        else:
            content = self.db.content
            content.insert(dict(item))
        return item
