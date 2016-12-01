"""Base test case"""

import unittest


class BaseTestCase(unittest.TestCase):
    """Base test case"""

    def assertEndsInR(self, seq):
        """Assert last element in sequence is r or R"""
        if seq[-1].lower() != 'r':
            raise AssertionError("{} does not end in 'r'".format(seq))
