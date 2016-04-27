import unittest

from framework.testbase import BaseTestCase
import utils.useless_util


class ExampleTestCase(BaseTestCase):

    @classmethod
    def setUpClass(cls):
        """runs before tests

        an exception here results in tests and tearDownClass not running"""
        pass
 
    @classmethod
    def tearDownClass(cls):
        """runs after tests"""
        pass

    def setUp(self):
        """setting up test"""
        pass

    def tearDown(self):
        """tearing down test

        only runs if setUp succeeds"""
        pass

    def test_sim2_config(self):
        """test is hardcoded to sim2_settings"""
        self.log.info("executing ExampleTestCase.test_sim2_config")
        self.assertEqual(self.settings['setting1'], 'default_setting1_value')
        self.assertEqual(self.settings['setting2'], 'sim2_setting2_valueOVERRIDE')
        self.assertEqual(self.settings['setting3'], 'sim2_setting3_valueOVERRIDE')

    def test_adding_ints(self):
        """demo using utility method"""
        self.log.info("executing ExampleTestCase.test_adding_ints")
        self.assertEqual(utils.useless_util.add_stuffs(42, 8), 50)

    def test_str_ends_in_r(self):
        """demo using custom assertion from base class"""
        self.log.info("executing ExampleTestCase.test_str_ends_in_r")
        self.assertEndsInR('Doctor')

    def test_fails(self):
        """test that fails"""
        self.log.info("executing ExampleTestCase.test_fails")
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_fails_failure_expected(self):
        """test fails where failure expected"""
        self.log.info("executing ExampleTestCase.test_fails_failure_expected")
        self.assertTrue(False)

    @unittest.expectedFailure
    def test_passes_failure_expected(self):
        """test passes where failure expected"""
        self.log.info("executing ExampleTestCase.test_passes_failure_expected")
        self.assertTrue(True)

    def test_error(self):
        """test that results in error"""
        self.log.info("executing ExampleTestCase.test_error")
        raise IOError

    @unittest.skip("skip this test")
    def test_skips(self):
        """test that is skipped"""
        self.log.info("executing ExampleTestCase.test_skips")
        pass

    def test_writes_stdout(self):
        """test which writes to stdout. see nosetests --nocapture option"""
        self.log.info("executing ExampleTestCase.test_writes_stdout")
        print "here's some text from tests.test_example:ExampleTestCase.test_writes_stdout"
        pass
