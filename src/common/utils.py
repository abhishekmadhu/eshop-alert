from passlib.hash import pbkdf2_sha512

__author__ = "abhishekmadhu"

class Utils(object):

    @staticmethod
    def hash_password(password):
        """

        :param password:
        :return: A sha512 -> pbksha512 encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """

        :param password:
        :param hashed_password:
        :return:
        """
        return pbkdf2_sha512.verify(password, hashed_password)
