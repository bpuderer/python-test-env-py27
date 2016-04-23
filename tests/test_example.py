import logging

import framework.config as config
from framework.testbase import BaseTestCase
import utils.useless_util


log = logging.getLogger(__name__)

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
        log.info("executing ExampleTestCase.test_sim2_config")
        self.assertEqual(config.props['setting1'], 'default_setting1_value')
        self.assertEqual(config.props['setting2'], 'sim2_setting2_valueOVERRIDE')
        self.assertEqual(config.props['setting3'], 'sim2_setting3_valueOVERRIDE')

    def test_adding_ints(self):
        """demo using utility method"""
        log.info("executing ExampleTestCase.test_adding_ints")
        self.assertEqual(utils.useless_util.add_stuffs(42, 8), 50)

    def test_str_ends_in_r(self):
        """demo using custom assertion from base class"""
        log.info("executing ExampleTestCase.test_str_ends_in_r")
        self.assertEndsInR('Doctor')
