"""Tests for useless_util"""

import unittest

from utils.useless_util import add_stuffs


class UselessUtilTestCase(unittest.TestCase):
    """Tests for useless_util.add_stuffs"""

    def test_adding_ints(self):
        """Test adding ints"""
        self.assertEqual(add_stuffs(-1, 5), 4)

    def test_concat_strings(self):
        """Test adding strings"""
        self.assertEqual(add_stuffs('Doc', 'tor'), 'Doctor')

    def test_merge_lists(self):
        """Test adding lists"""
        lista = [2001, 2010, 2112]
        listb = ['odyssey', 'odyssey two', 'solar fed']
        self.assertEqual(add_stuffs(lista, listb), lista + listb)
