import uuid

import requests
from bs4 import BeautifulSoup
import re
import src.models.items.constants as ItemConstants

from src.common.database import Database

__author__ = "abhishekmadhu"


class Item(object):
    def __init__(self, name, price, url, store, _id=None):
        self.name = name
        self.url = url
        self.store = store
        tag_name = store.tag_name
        query = store.query
        self.price = self.load_price(tag_name=tag_name, query=query)
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} costs {} at {}>".format(self.name, self.price, self.url)

    def load_price(self, tag_name, query):
        """
        Amazon:
        <span id="priceblock_ourprice" class="a-size-medium a-color-price">
            <span class="currencyINR">
                &nbsp;&nbsp;
            </span>
            219,000.00
        </span>
        :return:
        """
        request = requests.get(self.url)
        content = self.content
        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(tag_name, query)

        string_price = element.text.strip()

        pattern = re.compile("(\d+.\d+)")
        match = pattern.search(string_price)

        return match.group()

    def save_to_mongo(self):
        Database.insert(ItemConstants.COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url
        }

    def get_from_mongo(self):
        return Database.find_one(collection=ItemConstants.COLLECTIONS, query={"name": self.name})
