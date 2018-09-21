import datetime
import uuid
import src.models.alerts.constants as AlertConstants
import requests

from src.common.database import Database

__author__ = "abhishekmadhu"


class Alert(object):
    def __init__(self, user, price_limit, item, last_checked=None, _id=None):
        self.user = user
        self.price_limit = price_limit
        self.item = item
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Alert for Mr./Mrs. {} on {} under price {} rupees>".format(self.user.email, self.item.name, self.price_limit)

    def send(self):
        return requests.post(
            AlertConstants.URL,
            auth=("api", AlertConstants.API_KEY),
            data={
                "from": AlertConstants.FROM,
                "to": self.user.email,
                "subject": "Price limit reached for {}".format(self.item.name),
                "text": "We have found a deal for you (link here)."
            }
        )

    @classmethod
    def find_needing_update(cls, minutes_since_update=AlertConstants.ALERT_TIMEOUT):
        last_updated_limit = datetime.datetime.utcnow() - datetime.timedelta(minutes=minutes_since_update)
        return [cls(**element) for element in Database.find(AlertConstants.COLLECTION, {"last_checked": {"$gte": last_updated_limit}})]
