#!/usr/bin/python3
"""Unit test for Base class"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Unit test for Base class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.b1 = Base()
        self.b2 = Base(3)
        self.b3 = Base(3)
        self.b4 = Base()
        self.b5 = Base()

    def tearDown(self):
        """Unit test tear down"""
        print('tearDown')

    def test_module_docstring(self):
        """Module Docstring Check"""
        result = len(__import__('models.base').__doc__)
        self.assertTrue(result > 0, True)

#    def test_class_docstring(self):
#        """Class Docstring Check"""
#        result = len(__import__('models.base').Base.__doc__)
#        self.assertTrue(result > 0, True)

#    def test_function_docstring(self):
#        """Method/Function Docstring Check"""
#        result = len(__init__.__doc__)
#        self.assertTrue(result > 0, True)

    def test_init(self):
        """Test for init method"""
        print("test_init")
        self.assertIsNotNone(self.b1)
        self.assertIsInstance(self.b1, Base)
        self.assertEqual(self.b1.id, 1)

        self.assertIsNotNone(self.b2)
        self.assertIsInstance(self.b2, Base)
        self.assertEqual(self.b2.id, 3)

        self.assertIsNotNone(self.b3)
        self.assertIsInstance(self.b3, Base)
        self.assertEqual(self.b3.id, 2)

        self.assertIsNotNone(self.b4)
        self.assertIsInstance(self.b4, Base)
        self.assertEqual(self.b4.id, 4)

        self.assertIsNotNone(self.b5)
        self.assertIsInstance(self.b5, Base)
        self.assertEqual(self.b5.id, 5)
