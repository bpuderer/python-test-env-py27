import unittest


class BaseTestCase(unittest.TestCase):

    def assertEndsInR(self, seq):
        if seq[-1].lower() != 'r':
            raise AssertionError("{} does not end in 'r'".format(seq))
