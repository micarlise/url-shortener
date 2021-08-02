from pymongo import MongoClient


class db_client():
    def __init__(self):
        self.app = None
        self.driver = None

    def __connect__(self):
        self.driver = MongoClient('localhost', 27017)
        return self.driver

    def __call__(self):
        if not self.driver:
            return self.__connect__()
        return self.driver

    def init_db(self, app):
        self.app = app
        self.__connect__()


client = db_client()
