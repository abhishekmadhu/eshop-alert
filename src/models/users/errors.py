__author__ = "abhishekmadhu"


class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserDoesNotExistError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass