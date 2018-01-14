import httplib
import json

import requests

from framework.config import settings
from framework.testbase import BaseTestCase


class RestJsonExample(BaseTestCase):

    def setUp(self):
        """test setup"""
        self.remove_books()

    def tearDown(self):
        """test cleanup"""
        self.remove_books()

    @staticmethod
    def create_book(filename):
        with open(filename) as f:
            book = json.load(f)
        return requests.post(settings["books_url"], json=book, timeout=5)

    @staticmethod
    def remove_books():
        requests.delete(settings["books_url"], timeout=5)


    def test_book_creation(self):
        """verify book creation using httpsim.py in python-test"""

        r = self.create_book("resources/requests/books/request1.json")
        self.assertEqual(r.status_code, httplib.CREATED)
