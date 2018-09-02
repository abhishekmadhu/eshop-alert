__author__ = "abhishekmadhu"

class Alert(object):
    def __init__(self, user, price_limit, item):
        self.user = user
        self.price_limit = price_limit
        self.item = item

    def __repr__(self):
        return "<Alert for Mr./Mrs. {} on {} under price {} rupees>".format(self.user.email, self.item.name, self.price_limit)
