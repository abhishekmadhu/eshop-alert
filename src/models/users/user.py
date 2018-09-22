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
        :param email: The user_email's email
        :param password: A SHA512 hashed password the user_email sends by the login form
        :return: True if the combination is correct, else false
        """
        user_data = Database.find_one(collection='users', query={"email": email})
        if user_data is None:
            # Tell user_email that no account exists for that email
            raise UserErrors.UserDoesNotExistError('There is no user_email registered for this e-mail.')

        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell user_email that the password is wrong
            raise UserErrors.IncorrectPasswordError('The password is wrong.')

        return True

    @staticmethod
    def register_user(email, password):
        """

        :param email: user_email's preferred email
        :param password: sha512 hashed password
        :return: True if registered successfully, or raise known exceptions, or False otherwise
        """
        user_data = Database.find_one(collection='users', query={"email": email})

        if user_data is not None:
            # Tell the user_email that they are already registered
            raise UserErrors.UserAlreadyRegisteredError("An user_email already exists for this e-mail.")

        if not Utils.email_is_valid(email):
            # Tell the user_email that the email is not constructed properly
            raise UserErrors.InvalidEmailError('Incorrect email format (yourname@yourdomain.com)')

        User(email=email, password=Utils.hash_password(password)).save_to_db()

        return True

    def save_to_db(self):
        Database.insert(collection='users', data=self.json())

    def json(self):
        return {"_id": self._id,
                "email": self.email,
                "password": self.password
        }