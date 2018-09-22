import pymongo

# contains functions that can be used in the Database
__author__ = "abhishekmadhu"


class Database(object):
    URI = "mongodb://127.0.0.1:27017"  # keeping these same for all db
    DATABASE = None

    @staticmethod   # to not use self, as this belongs to whole db class and not to a single instance only
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def count(collection, query):
        return Database.DATABASE[collection].count(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)

    ########################################################

    @staticmethod
    def update_last_checked(collection, _id, last_checked):
        Database.DATABASE[collection].update(
            {"_id": _id},
            {
                "$set": {
                    "last_checked": last_checked
                }
            })

    @staticmethod
    def update_price(collection, _id, price):       # redundant now, remove after completion
        Database.DATABASE[collection].update(
            {"_id": _id},
            {
                "$set": {
                    "price": price
                }
            })