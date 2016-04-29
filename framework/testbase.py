import logging
import unittest

import config


class BaseTestCase(unittest.TestCase):

    settings = config.settings
    log = logging.getLogger(__name__)

    def assertEndsInR(self, seq):
        if seq[-1].lower() != 'r':
            raise AssertionError("{} does not end in 'r'".format(seq))
