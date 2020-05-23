#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit test for max integer
    """

    def test_valid(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 8, 4, 6, 3, 8]), 8)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([5]), 5)

    def test_none(self):
        self.assertIsNone(max_integer())

    def test_type(self):
        self.assertRaises(Exception, max_integer, ["string", 3.14, (0, 0)])
