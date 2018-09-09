import uuid

import requests
import re
import src.models.items.constants as ItemConstants

from bs4 import BeautifulSoup
from src.common.database import Database
from src.models.stores.store import Store

__author__ = "abhishekmadhu"


class Item(object):
    def __init__(self, name, url, _id=None):
        self.name = name
        self.url = url
        store = Store.find_by_url(url)
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
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        soup = soup if soup is not None else "This is an empty soup"

        print(soup)         #

        element = soup.find(tag_name, query)        # cannot find this tag
        element = element if element is not None else "The element variable is a Nonetype object as soup.find() returned None"

        print(element)      #

        if element is not None:
            string_price = element.text.strip()
            pattern = re.compile("(\d+.\d+)")
            match = pattern.search(string_price)
            return match.group()
        else:
            print("Stopping, as element variable is None!")

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
