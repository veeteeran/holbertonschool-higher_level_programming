#!/usr/bin/python3
"""Unit test for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Unit test for Rectangle class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(3, 5, 0, 0, 12)
        self.r4 = Rectangle(9, 6, 4, 3, 12)
        self.r5 = Rectangle(1, 6, 1, 2, 1)
        self.r6 = Rectangle(9, 6, 0, 8)

    def tearDown(self):
        """Unit test tear down"""
        print('tearDown')

    def test_init(self):
        """Test for init method"""
        print("test_init")
        # r1 tests
        self.assertIsNotNone(self.r1)
        self.assertIsInstance(self.r1, Base)
        self.assertIs(type(self.r1), Rectangle)
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        # r2 tests
        self.assertIsNotNone(self.r2)
        self.assertIsInstance(self.r2, Base)
        self.assertIs(type(self.r2), Rectangle)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)
        with self.assertRaises(TypeError):
            self.r2.__init__("string", 4)
        with self.assertRaises(TypeError):
            self.r2.__init__([1, 2, 3], 4)
        with self.assertRaises(TypeError):
            self.r2.__init__()

        # r3 tests
        self.assertIsNotNone(self.r3)
        self.assertIsInstance(self.r3, Base)
        self.assertIs(type(self.r3), Rectangle)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)
        with self.assertRaises(TypeError):
            self.r3.__init__(3, True)
        with self.assertRaises(TypeError):
            self.r3.__init__(3, (1, ))

        # r4 tests
        self.assertIsNotNone(self.r4)
        self.assertIsInstance(self.r4, Base)
        self.assertIs(type(self.r4), Rectangle)
        self.assertEqual(self.r4.id, 3)
        self.assertEqual(self.r4.width, 9)
        self.assertEqual(self.r4.height, 6)
        self.assertEqual(self.r4.x, 4)
        self.assertEqual(self.r4.y, 3)

        with self.assertRaises(ValueError):
            self.r4.__init__(0, 4)
        with self.assertRaises(ValueError):
            self.r4.__init__(-1, 4)

        # r5 tests
        self.assertIsNotNone(self.r5)
        self.assertIsInstance(self.r5, Base)
        self.assertIs(type(self.r5), Rectangle)
        self.assertEqual(self.r5.id, 4)
        self.assertEqual(self.r5.width, 1)
        self.assertEqual(self.r5.height, 6)
        self.assertEqual(self.r5.x, 1)
        self.assertEqual(self.r5.y, 2)

        with self.assertRaises(ValueError):
            self.r5.__init__(1, 0)
        with self.assertRaises(ValueError):
            self.r5.__init__(1, -6)

        # r6 tests
        self.assertIsNotNone(self.r6)
        self.assertIsInstance(self.r6, Base)
        self.assertIs(type(self.r6), Rectangle)
        self.assertEqual(self.r6.id, 5)
        self.assertEqual(self.r6.width, 9)
        self.assertEqual(self.r6.height, 6)
        self.assertEqual(self.r6.x, 0)
        self.assertEqual(self.r6.y, 8)

    def test_validate_attributes(self):
        """Test exceptions are raised when attribute invalid"""


        with self.assertRaises(ValueError):
            self.r6.__init__(9, 6, -3)

        with self.assertRaises(ValueError):
            self.r6.__init__(9, 6, 0, -8)
