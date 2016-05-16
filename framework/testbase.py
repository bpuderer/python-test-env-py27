"""Base test case."""

import logging
import unittest

import framework.config


class BaseTestCase(unittest.TestCase):
    """Base test case the tests can subclass."""
    settings = framework.config.settings
    log = logging.getLogger(__name__)

    def assertEndsInR(self, seq):
        """Assert last element in sequence is r or R."""
        if seq[-1].lower() != 'r':
            raise AssertionError("{} does not end in 'r'".format(seq))
