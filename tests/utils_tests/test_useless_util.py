from framework.testbase import BaseTestCase
import utils.useless_util


class UselessUtilTestCase(BaseTestCase):

    def test_adding_ints(self):
        """utility functions should have tests too.  adding ints"""
        self.log.info("executing UselessUtilTestCase.test_adding_ints")
        self.assertEqual(utils.useless_util.add_stuffs(-1, 5), 4)

    def test_concat_strings(self):
        """utility functions should have tests too.  concat strings"""
        self.log.info("executing UselessUtilTestCase.test_concat_strings")
        self.assertEqual(utils.useless_util.add_stuffs('Doc', 'tor'), 'Doctor')

    def test_merge_lists(self):
        """utility functions should have tests too.  merge lists"""
        self.log.info("executing UselessUtilTestCase.test_merge_lists")
        lista = [2001, 2010, 2112]
        listb = ['odyssey', 'odyssey two', 'solar fed']
        expected = [2001, 2010, 2112, 'odyssey', 'odyssey two', 'solar fed']
        self.assertEqual(utils.useless_util.add_stuffs(lista, listb), expected)
