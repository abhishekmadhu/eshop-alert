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
        