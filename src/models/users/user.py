__author__ = "abhishekmadhu"

class User(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Email: {} & PWD: {}>".format(seld.email, self.password)
