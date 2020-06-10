#!/usr/bin/python3
"""Unit test for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import pep8


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
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)

    def tearDown(self):
        """Unit test tear down"""
        print('tearDown')

    def test_a_init(self):
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

    def test_b_to_json_string(self):
        """Test for to_json_string method"""
        print("test_to_json_string")
        dictionary = self.r1.to_dictionary()
        expected = {'x': 2, 'width': 10, 'id': 11, 'height': 7, 'y': 8}
        self.assertEqual(dictionary, expected)
        self.assertIs(type(dictionary), dict)
        json_string = Base.to_json_string([dictionary])
        output = '[{"x": 2, "width": 10, "id": 11, "height": 7, "y": 8}]'
        self.assertEqual(len(json_string), len(output))
        self.assertIs(type(json_string), str)

        empty_dict = None
        empty_str = Base.to_json_string(empty_dict)
        self.assertEqual(empty_str, "[]")

        empty_dict = []
        empty_str = Base.to_json_string(empty_dict)
        self.assertEqual(empty_str, "[]")

    def test_c_save_to_file(self):
        """Test for save_to_file method"""
        print("test_save_to_file")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file([self.r1, self.r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 107)

    def test_d_from_json_string(self):
        """Test for from_json_string method"""
        print("test_from_json_string")

        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])

        list_output = Rectangle.from_json_string("")
        self.assertEqual(list_output, [])

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIs(type(list_output), list)
        self.assertEqual(len(list_output[0]), len(list_input[0]))
        self.assertEqual(len(list_output[1]), len(list_input[1]))

    def test_e_create(self):
        """Test for create method"""
        print("test_create")
        self.r3 = Rectangle(3, 5, 1)
        self.assertEqual(self.r3.__str__(), '[Rectangle] (50) 1/0 - 3/5')
        r3_dictionary = self.r3.to_dictionary()
        self.r4 = Rectangle.create(**r3_dictionary)
        self.assertEqual(self.r3.__str__(), '[Rectangle] (50) 1/0 - 3/5')

        self.assertFalse(self.r3 is self.r4)
        self.assertFalse(self.r3 == self.r4)

    def test_f_load_from_file(self):
        """Test for load_from_file method"""
        print("test_load_from_file")
        list_rectangles_input = [self.r1, self.r2]

        Rectangle.save_to_file(list_rectangles_input)

        r_output = Rectangle.load_from_file()
        self.assertEqual(self.r1.__str__(), r_output[0].__str__())
        self.assertEqual(self.r2.__str__(), r_output[1].__str__())
        self.assertFalse(self.r1 is r_output[0])
        self.assertFalse(self.r2 == r_output[1])

        list_squares_input = [self.s1, self.s2]

        Square.save_to_file(list_squares_input)
        s_output = Square.load_from_file()
        self.assertEqual(self.s1.__str__(), s_output[0].__str__())
        self.assertEqual(self.s2.__str__(), s_output[1].__str__())
        self.assertFalse(self.s1 is s_output[0])
        self.assertFalse(self.s2 == s_output[1])

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

    def test_pep8_conformance(self):
        """load_from_file Docstring Test"""
        print("test_test_pep8_conformance")
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)
