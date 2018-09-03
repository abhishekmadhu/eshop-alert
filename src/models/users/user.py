import uuid

from src.common.database import Database
from src.common.utils import Utils
import src.models.users.errors as UserErrors

__author__ = "abhishekmadhu"


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Email: {} & PWD: {}>".format(self.email, self.password)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies whether a given email-password combination [as sent by the login form]
        is valid or not.
        :param email: The user's email
        :param password: A SHA512 hashed password the user sends by the login form
        :return: True if the combination is correct, else false
        """
        user_data = Database.find_one(collection='users', query={"email": email})
        if user_data is None:
            # Tell user that no account exists for that email
            raise UserErrors.UserDoesNotExistError('There is no user registered for this e-mail.')

        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user that the password is wrong
            raise UserErrors.IncorrectPasswordError('The password is wrong.')

        return True
