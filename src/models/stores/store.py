import uuid
import src.models.stores.constants as StoreConstants
from src.common.database import Database
import src.models.stores.errors as StoreErrors

__author__ = "abhishekmadhu"


class Store(object):
    def __init__(self, name, url_prefix, tag_name, query, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Store Name: {}\nurl_prefix: {}\ntagname: {}\nquery: {}\n_id: {}>".format(self.name,
                                                                                          self.url_prefix,
                                                                                          self.tag_name,
                                                                                          self.query,
                                                                                          self._id)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StoreConstants.COLLECTION, {"_id": id}))

    def save_to_mongo(self):
        Database.insert(collection=StoreConstants.COLLECTIONS, data=self.json())

    @classmethod
    def get_by_name(cls, name):
        return cls(**Database.find_one(StoreConstants, {"name": name}))

    @classmethod
    def get_by_url_prefix(cls, url_prefix):
        """
        matches the url prefix with those in the database, and tries
        to decide which predefined store it is.

        example: if we pass "http://www.joh" as url_prefix
        :param url_prefix: "http://www.joh"
        :return: object from database where the url_prefix starts with "http://www.johnlewis.com"
                * If two entries match, NO IDEA what is gonna happen [LOL]
        """
        return cls(**Database.find_one(StoreConstants.COLLECTIONS, {"url_prefix": {"$regex": '^{}'.format(url_prefix)}}))

    @classmethod
    def find_by_url(cls, url):
        """

        :param url:
        :return:
        """
        for i in range(1, len(url)+1):
            try:
                store = cls.get_by_url_prefix(url[:i])
                return store
            except:
                # return None
                # a method returns None by default. So if we put pass, it returns None [tip to read others' code]
                # pass
                return StoreErrors.StoreNotFoundException("The url_prefix did not give us any results!")
