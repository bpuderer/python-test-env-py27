from framework.testbase import BaseTestCase


class ExampleTestCase2(BaseTestCase):

    def test_foo(self):
        """test_foo desc"""
        self.log.info("executing ExampleTestCase2.test_foo")
        self.assertTrue(1)
