import logging

from framework.testbase import BaseTestCase


log = logging.getLogger(__name__)

class ExampleTestCase2(BaseTestCase):

    def test_foo(self):
        """test_foo desc"""
        log.info("executing ExampleTestCase2.test_foo")
        self.assertTrue(1)
