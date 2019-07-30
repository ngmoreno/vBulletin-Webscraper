# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
#from scrapy import log

class MongoDBPipeline(object):
  collection_name = 'posts'

  # Default __init__()
  def __init__(self, mongo_uri, mongo_db):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db

  @classmethod
  def from_crawler(cls, crawler):
    return cls(
      mongo_uri=crawler.settings.get('MONGO_URI'),
      mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    )

  def open_spider(self, spider):
    #self.client = pymongo.MongoClient(self.mongo_uri,27017)
    self.client = pymongo.MongoClient('127.0.0.1',27017)
    
    # TODO: Enter mongo database to be used 
    self.db = self.client.databaseGoesHere
    
    self.coll = self.db.posts
    print "MONGODB IS OPENED\n"

  def close_spider(self, spider):
    self.client.close()
    print "MONGODB IS CLOSED\n"

  def process_item(self, item, spider):
    print "MONGODB IS PROCESSING ITEM\n"
    print item
    (self.coll).insert_one(dict(item))
    return item
