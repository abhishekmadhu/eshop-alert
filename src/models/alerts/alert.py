import uuid

__author__ = "abhishekmadhu"

class Alert(object):
    def __init__(self, user, price_limit, item, _id=None):
        self.user = user
        self.price_limit = price_limit
        self.item = item
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Alert for Mr./Mrs. {} on {} under price {} rupees>".format(self.user.email, self.item.name, self.price_limit)
