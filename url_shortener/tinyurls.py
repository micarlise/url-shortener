from secrets import token_urlsafe
from . import db


class tiny_url:

    def __init__(self):
        self._driver = db.client()
        self._collection = self._get_collection()

        self._only_urls = {
            '_id': 0,
            'url': 1
        }

    def _get_collection(self):
        return self._driver['tinyurls']['shortkeys']

    def _generate_key(self):
        return token_urlsafe(8)

    def insert_url(self, url):
        query = {
            'shortkey': self._generate_key(),
            'url': url
        }

        if self._collection.insert_one(query):
            return 201
        return 500

    def lookup_key(self, key):
        query = {
            'shortkey': key
        }

        r = self._collection.find_one(query, projection=self._only_urls)

        if r:
            return r['url']
        return None

    def get_all_urls(self):
        return {x['shortkey']: x['url'] for x in self._collection.find()}
