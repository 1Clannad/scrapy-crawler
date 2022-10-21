# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class MongoDemo1Pipeline(object):
    def open_spider(self.response):
        self.client = Mongoclient()
        self.db = self.client.information
        self.collection = self.db.collection

    def process_item(self, item, spider):
        self.collecion.insert(item)
        return item
    def colse_spider(self.spider):
        self.client.close()
