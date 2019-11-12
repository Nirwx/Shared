from pymongo import MongoClient

# Remote
# client = MongoClient(IP, 27017)
# db = client.testDB
# collection = db.collectionTest1

# Local
class MongoConnection():
    def __init__(self):
        self.client = MongoClient('127.0.0.1', 27017)
        self.db = self.client.testDB

    def find_one(self, collection, param = {}):
        doc = self.db[collection].find_one(param)
        return  doc

    def find_time_range(self, collection, time_a, time_b):
        doc = self.db[collection].find({"insert_time":{'$gte': time_a,'$lt': time_b }})
        return doc

    def insert_one(self, collection, doc):
        self.db[collection].insert(doc)

    def find_test(self):
        data = self.db.store_info.find_one({})

# posts = db.doc
# db.doc.insert_one(doc).inserted_id