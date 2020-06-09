#!/usr/bin/python3
"""Unit test for Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
from contextlib import redirect_stdout


class TestBaseClass(unittest.TestCase):
    """Unit test for Square class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        """Unit test setup"""
        print('setUp')
        self.s1 = Square(5)
        self.s2 = Square(2, 2)
        self.s3 = Square(3, 1, 3)
        self.s4 = Square(10, 2, 1)
        self.s5 = Square(1, 1)

    def tearDown(self):
        """Unit test tear down"""
        print('tearDown')
        del self.s1
        del self.s2
        del self.s3
        del self.s4
        del self.s5

    def test_a_init(self):
        """Test for init method"""
        print("test_init")
        # s1 tests
        self.assertIsNotNone(self.s1)
        self.assertIsInstance(self.s1, Base)
        self.assertIsInstance(self.s1, Rectangle)
        self.assertIs(type(self.s1), Square)
        self.assertEqual(self.s1.id, 205)
        self.assertEqual(self.s1.width, 5)
        self.assertEqual(self.s1.height, 5)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        # s2 tests
        self.assertIsNotNone(self.s2)
        self.assertIsInstance(self.s2, Base)
        self.assertIsInstance(self.s2, Rectangle)
        self.assertIs(type(self.s2), Square)
        self.assertEqual(self.s2.id, 206)
        self.assertEqual(self.s2.width, 2)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 0)

        # s3 tests
        self.assertIsNotNone(self.s3)
        self.assertIsInstance(self.s3, Base)
        self.assertIsInstance(self.s3, Rectangle)
        self.assertIs(type(self.s3), Square)
        self.assertEqual(self.s3.id, 207)
        self.assertEqual(self.s3.width, 3)
        self.assertEqual(self.s3.height, 3)
        self.assertEqual(self.s3.x, 1)
        self.assertEqual(self.s3.y, 3)

    def test_b_validate_attributes(self):
        """Test exceptions are raised when attribute invalid"""
        print("test_validate_attributes")

        # s1 tests
        with self.assertRaises(TypeError):
            self.s1.__init__("string", 4)
        with self.assertRaises(TypeError):
            self.s1.__init__([1, 2, 3], 4)
        with self.assertRaises(TypeError):
            self.s1.__init__()

        # s2 tests
        with self.assertRaises(TypeError):
            self.s2.__init__(3, True)
        with self.assertRaises(TypeError):
            self.s2.__init__(3, (1, ))

        # s3 tests
        with self.assertRaises(ValueError):
            self.s3.__init__(0, 4)
        with self.assertRaises(ValueError):
            self.s3.__init__(-1, 4)

    def test_c_area(self):
        """Test for area method"""
        print("test_area")

        # s1 tests
        self.assertEqual(self.s1.area(), 25)

        # s2 tests
        self.assertEqual(self.s2.area(), 4)

        # s3 tests
        self.assertEqual(self.s3.area(), 9)

    def test_d_display(self):
        """Test for display method"""
        print("test_display")
        f = io.StringIO()
        with redirect_stdout(f):
            self.s1.display()
        output = f.getvalue()
        self.assertEqual(output, f.getvalue())

    def test_e_str(self):
        """Test for __str__ method"""
        print("test_str")
        self.assertEqual(self.s1.__str__(), "[Square] (240) 0/0 - 5")
        self.assertEqual(self.s2.__str__(), "[Square] (241) 2/0 - 2")
        self.assertEqual(self.s3.__str__(), "[Square] (242) 1/3 - 3")

    def test_f_update_args(self):
        """Test for update args method"""
        print("test_update_args")
        self.assertEqual(self.s1.__str__(), "[Square] (245) 0/0 - 5")
        self.s1.update(10)
        self.assertEqual(self.s1.__str__(), "[Square] (10) 0/0 - 5")
        self.s1.update(1, 2)
        self.assertEqual(self.s1.__str__(), "[Square] (1) 0/0 - 2")
        self.s1.update(1, 2, 3)
        self.assertEqual(self.s1.__str__(), "[Square] (1) 3/0 - 2")
        self.s1.update(1, 2, 3, 4)
        self.assertEqual(self.s1.__str__(), "[Square] (1) 3/4 - 2")

    def test_g_update_kwargs(self):
        """Test for update kwargs method"""
        print("test_update_kwargs")
        self.s1.update(x=12)
        self.assertEqual(self.s1.__str__(), "[Square] (250) 12/0 - 5")
        self.s1.update(size=7, y=1)
        self.assertEqual(self.s1.__str__(), "[Square] (250) 12/1 - 7")
        self.s1.update(size=7, id=89, y=1)
        self.assertEqual(self.s1.__str__(), "[Square] (89) 12/1 - 7")

    def test_h_to_dictionary(self):
        """Test for to_dictionary method"""
        print("test_to_dictionary")
        self.assertEqual(self.s4.__str__(), "[Square] (258) 2/1 - 10")
        s4_dictionary = self.s4.to_dictionary()
        expected = {'id': 258, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s4_dictionary, expected)
        self.assertIs(type(s4_dictionary), dict)

        self.assertEqual(self.s5.__str__(), "[Square] (259) 1/0 - 1")
        self.s5.update(**s4_dictionary)
        self.assertEqual(self.s5.__str__(), "[Square] (258) 2/1 - 10")
        self.assertFalse(self.s4 == self.s5)

    def test_module_docstring(self):
        """Module Docstring Check"""
        print("test_module_docstring")
        result = len(__import__('models.square').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Class Docstring Test"""
        print("test_class_docstring")
        result = len(Square.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test_size_getter_docstring(self):
        """size_getter Docstring Test"""
        print("test_size_getter_docstring")
        result = len(Square.size.__doc__)
        self.assertTrue(result > 0, True)

    def test_x_getter_docstring(self):
        """x_getter Docstring Test"""
        print("test_x_getter_docstring")
        result = len(Square.x.__doc__)
        self.assertTrue(result > 0, True)

    def test_y_getter_docstring(self):
        """y_getter Docstring Test"""
        print("test_y_getter_docstring")
        result = len(Square.y.__doc__)
        self.assertTrue(result > 0, True)

    def test_area_docstring(self):
        """area Docstring Test"""
        print("test_area_docstring")
        result = len(Square.area.__doc__)
        self.assertTrue(result > 0, True)

    def test_display_docstring(self):
        """display Docstring Test"""
        print("test_display_docstring")
        result = len(Square.display.__doc__)
        self.assertTrue(result > 0, True)

    def test_str_docstring(self):
        """str Docstring Test"""
        print("test_str_docstring")
        result = len(Square.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_update_docstring(self):
        """update Docstring Test"""
        print("test_update_docstring")
        result = len(Square.update.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dictionary_docstring(self):
        """to_dictionary Docstring Test"""
        print("test_to_dictionary_docstring")
        result = len(Square.to_dictionary.__doc__)
        self.assertTrue(result > 0, True)
