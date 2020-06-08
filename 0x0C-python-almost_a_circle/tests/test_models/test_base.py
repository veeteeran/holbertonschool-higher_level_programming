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
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

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
        self.assertEqual(self.b3.id, 3)

        self.assertIsNotNone(self.b4)
        self.assertIsInstance(self.b4, Base)
        self.assertEqual(self.b4.id, 2)

        self.assertIsNotNone(self.b5)
        self.assertIsInstance(self.b5, Base)
        self.assertEqual(self.b5.id, 3)

    def test_module_docstring(self):
        """Module Docstring Check"""
        print("test_module_docstring")
        result = len(__import__('models.base').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Class Docstring Test"""
        print("test_class_docstring")
        result = len(Base.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_json_string_docstring(self):
        """to_json_string Docstring Test"""
        print("test_to_json_string_docstring")
        result = len(Base.to_json_string.__doc__)
        self.assertTrue(result > 0, True)

    def test_save_to_file_docstring(self):
        """save_to_file Docstring Test"""
        print("test_save_to_file_docstring")
        result = len(Base.save_to_file.__doc__)
        self.assertTrue(result > 0, True)

    def test_from_json_string_docstring(self):
        """from_json_string Docstring Test"""
        print("test_from_json_string_docstring")
        result = len(Base.from_json_string.__doc__)
        self.assertTrue(result > 0, True)

    def test_create_docstring(self):
        """create Docstring Test"""
        print("test_create_docstring")
        result = len(Base.create.__doc__)
        self.assertTrue(result > 0, True)

    def test_load_from_file_docstring(self):
        """load_from_file Docstring Test"""
        print("test_load_from_file_docstring")
        result = len(Base.load_from_file.__doc__)
        self.assertTrue(result > 0, True)
