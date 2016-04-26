import logging
import unittest

import config


class BaseTestCase(unittest.TestCase):

    log = logging.getLogger(__name__)
    settings = config.settings

    def assertEndsInR(self, seq):
        if seq[-1].lower() != 'r':
            raise AssertionError("{} does not end in 'r'".format(seq))
