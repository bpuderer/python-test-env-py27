"""Demo basics of using test environment"""

import logging
import unittest

from framework.config import settings
from framework.testbase import BaseTestCase
from utils.useless_util import add_stuffs

log = logging.getLogger(__name__)


class ExampleTestCase(BaseTestCase):
    """Demo basics of using test environment."""

    @classmethod
    def setUpClass(cls):
        """setUpClass runs before tests.

        An exception here results in tests and tearDownClass not running."""
        pass

    @classmethod
    def tearDownClass(cls):
        """tearDownClass runs after tests"""
        pass

    def setUp(self):
        """setUp runs before each test.

        An exception here results in test and tearDown not running."""
        pass

    def tearDown(self):
        """tearDown runs after each test"""
        pass

    def test_env1_config(self):
        """Demo accessing settings"""
        log.info("Test settings: " + str(settings))
        self.assertEqual(settings['setting1'], 'env1_setting1_value')
        self.assertEqual(settings['setting2'], 'default_setting2_value')

    def test_adding_ints(self):
        """Demo calling utility method"""
        log.info("executing ExampleTestCase.test_adding_ints")
        self.assertEqual(add_stuffs(42, 8), 50)

    def test_str_ends_in_r(self):
        """Demo custom assertion from BaseTestCase"""
        log.info("executing ExampleTestCase.test_str_ends_in_r")
        self.assertEndsInR('Doctor')

    def test_fails(self):
        """Demo test failure"""
        log.info("executing ExampleTestCase.test_fails")
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_fails_failure_expected(self):
        """Demo expected failure decorator where test fails"""
        log.info("executing ExampleTestCase.test_fails_failure_expected")
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_passes_failure_expected(self):
        """Demo expected failure decorator where test passes"""
        log.info("executing ExampleTestCase.test_passes_failure_expected")
        self.assertTrue(True)

    def test_error(self):
        """Demo test error"""
        log.info("executing ExampleTestCase.test_error")
        raise IOError

    @unittest.skip("skip this test")
    def test_skips(self):
        """Demo skipping a test using skip decorator"""
        log.info("executing ExampleTestCase.test_skips")

    def test_writes_stdout(self):
        """Demo test writing to stdout. See nosetests --nocapture option"""
        log.info("executing ExampleTestCase.test_writes_stdout")
        print "here's some text from tests.test_example:ExampleTestCase.test_writes_stdout"

    def test_accessing_resource(self):
        """Demo accessing a file in resources directory"""
        with open('resources/neededfile.txt') as f:
            log.info(f.read())

    def test_logging(self):
        """Demo logging"""
        log.debug("debug level message")
        log.info("info level message")
        log.warning("warning level message")
        log.error("error level message")
        log.critical("critical level message")
