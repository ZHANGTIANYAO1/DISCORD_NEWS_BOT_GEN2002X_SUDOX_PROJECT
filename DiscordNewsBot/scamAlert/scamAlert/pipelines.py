# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from itemadapter import ItemAdapter


class ScamalertPipeline:
    def __init__(self):
        MONGO_HOST = "127.0.0.1"  # IP, change to your database IP
        MONGO_PORT = 27017  # Port Number, change to your database port number
        MONGO_DB = "db2"  # database name, change to your database name
        MONGO_COLL = "db2"  # collection name, change to your collection name
        self.client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        self.client = pymongo.MongoClient()
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLL]

    def process_item(self, item, spider):
        title = item.get('title')

        # Check whether a news item with the same 'title' already exists in the database
        existing_item = self.collection.find_one({'title': title})

        if not existing_item:
            # If no item with the same title exists, insert the current item into the database
            self.collection.insert_one(dict(item))

        return item
