#!/usr/bin/python3
"""Unit test for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
from contextlib import redirect_stdout
import pep8


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
        self.r7 = Rectangle(10, 2, 1, 9)
        self.r8 = Rectangle(1, 1)

    def tearDown(self):
        """Unit test tear down"""
        print('tearDown')

    def test_a_init(self):
        """Test for init method"""
        print("test_init")
        # r1 tests
        self.assertIsNotNone(self.r1)
        self.assertIsInstance(self.r1, Base)
        self.assertIs(type(self.r1), Rectangle)
        self.assertEqual(self.r1.id, 112)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        # r2 tests
        self.assertIsNotNone(self.r2)
        self.assertIsInstance(self.r2, Base)
        self.assertIs(type(self.r2), Rectangle)
        self.assertEqual(self.r2.id, 113)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)

        # r3 tests
        self.assertIsNotNone(self.r3)
        self.assertIsInstance(self.r3, Base)
        self.assertIs(type(self.r3), Rectangle)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)

        # r4 tests
        self.assertIsNotNone(self.r4)
        self.assertIsInstance(self.r4, Base)
        self.assertIs(type(self.r4), Rectangle)
        self.assertEqual(self.r4.id, 12)
        self.assertEqual(self.r4.width, 9)
        self.assertEqual(self.r4.height, 6)
        self.assertEqual(self.r4.x, 4)
        self.assertEqual(self.r4.y, 3)

        # r5 tests
        self.assertIsNotNone(self.r5)
        self.assertIsInstance(self.r5, Base)
        self.assertIs(type(self.r5), Rectangle)
        self.assertEqual(self.r5.id, 1)
        self.assertEqual(self.r5.width, 1)
        self.assertEqual(self.r5.height, 6)
        self.assertEqual(self.r5.x, 1)
        self.assertEqual(self.r5.y, 2)

        # r6 tests
        self.assertIsNotNone(self.r6)
        self.assertIsInstance(self.r6, Base)
        self.assertIs(type(self.r6), Rectangle)
        self.assertEqual(self.r6.id, 114)
        self.assertEqual(self.r6.width, 9)
        self.assertEqual(self.r6.height, 6)
        self.assertEqual(self.r6.x, 0)
        self.assertEqual(self.r6.y, 8)

    def test_b_validate_attributes(self):
        """Test exceptions are raised when attribute invalid"""
        print("test_validate_attributes")
        # r2 tests
        with self.assertRaises(TypeError):
            self.r2.__init__("string", 4)
        with self.assertRaises(TypeError):
            self.r2.__init__([1, 2, 3], 4)
        with self.assertRaises(TypeError):
            self.r2.__init__()

        # r3 tests
        with self.assertRaises(TypeError):
            self.r3.__init__(3, True)
        with self.assertRaises(TypeError):
            self.r3.__init__(3, (1, ))

        # r4 tests
        with self.assertRaises(ValueError):
            self.r4.__init__(0, 4)
        with self.assertRaises(ValueError):
            self.r4.__init__(-1, 4)

        # r5 tests
        with self.assertRaises(ValueError):
            self.r5.__init__(1, 0)
        with self.assertRaises(ValueError):
            self.r5.__init__(1, -6)

        # r6 tests
        with self.assertRaises(ValueError):
            self.r6.__init__(9, 6, -3)

        with self.assertRaises(ValueError):
            self.r6.__init__(9, 6, 0, -8)

    def test_c_area(self):
        """Test for area method"""
        print("test_area")
        # r1 tests
        self.assertEqual(self.r1.area(), 20)

        # r2 tests
        self.assertEqual(self.r2.area(), 20)

        # r3 tests
        self.assertEqual(self.r3.area(), 15)

        # r4 tests
        self.assertEqual(self.r4.area(), 54)

        # r5 tests
        self.assertEqual(self.r5.area(), 6)

        # r6 tests
        self.assertEqual(self.r6.area(), 54)

    def test_d_display(self):
        """Test for display method"""
        print("test_display")
        f = io.StringIO()
        with redirect_stdout(f):
            self.r1.display()
        output = f.getvalue()
        self.assertEqual(output, f.getvalue())

    def test_e_str(self):
        """Test for __str__ method"""
        print("test_str")
        self.assertEqual(self.r1.__str__(), "[Rectangle] (147) 0/0 - 10/2")
        self.assertEqual(self.r2.__str__(), "[Rectangle] (148) 0/0 - 2/10")
        self.assertEqual(self.r3.__str__(), "[Rectangle] (12) 0/0 - 3/5")
        self.assertEqual(self.r4.__str__(), "[Rectangle] (12) 4/3 - 9/6")
        self.assertEqual(self.r5.__str__(), "[Rectangle] (1) 1/2 - 1/6")
        self.assertEqual(self.r6.__str__(), "[Rectangle] (149) 0/8 - 9/6")

    def test_f_update_args(self):
        """Test for update args method"""
        print("test_update_args")
        self.assertEqual(self.r1.__str__(), "[Rectangle] (152) 0/0 - 10/2")
        self.r1.update(89)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 10/2")
        self.r1.update(89, 2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/2")
        self.r1.update(89, 2, 3)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 0/0 - 2/3")
        self.r1.update(89, 2, 3, 4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 4/0 - 2/3")
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_g_update_kwargs(self):
        """Test for update kwargs method"""
        print("test_update_kwargs")
        self.assertEqual(self.r1.__str__(), "[Rectangle] (157) 0/0 - 10/2")
        self.r1.update(height=1)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (157) 0/0 - 10/1")
        self.r1.update(width=1, x=2)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (157) 2/0 - 1/1")
        self.r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        self.r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.r1.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    def test_h_to_dictionary(self):
        """Test for to_dictionary method"""
        print("test_to_dictionary")
        self.assertEqual(self.r7.__str__(), "[Rectangle] (165) 1/9 - 10/2")
        r7_dictionary = self.r7.to_dictionary()
        expected = {'x': 1, 'y': 9, 'id': 165, 'height': 2, 'width': 10}
        self.assertEqual(r7_dictionary, expected)
        self.assertIs(type(r7_dictionary), dict)

        self.assertEqual(self.r8.__str__(), "[Rectangle] (166) 0/0 - 1/1")
        self.r8.update(**r7_dictionary)
        self.assertEqual(self.r8.__str__(), "[Rectangle] (165) 1/9 - 10/2")
        self.assertFalse(self.r7 == self.r8)

    def test_module_docstring(self):
        """Module Docstring Check"""
        print("test_module_docstring")
        result = len(__import__('models.rectangle').__doc__)
        self.assertTrue(result > 0, True)

    def test_class_docstring(self):
        """Class Docstring Test"""
        print("test_class_docstring")
        result = len(Rectangle.__doc__)
        self.assertTrue(result > 0, True)

    def test_init_docstring(self):
        """init Docstring Test"""
        print("test_init_docstring")
        result = len(self.__init__.__doc__)
        self.assertTrue(result > 0, True)

    def test_width_getter_docstring(self):
        """width_getter Docstring Test"""
        print("test_width_getter_docstring")
        result = len(Rectangle.width.__doc__)
        self.assertTrue(result > 0, True)

    def test_height_getter_docstring(self):
        """height_getter Docstring Test"""
        print("test_height_getter_docstring")
        result = len(Rectangle.height.__doc__)
        self.assertTrue(result > 0, True)

    def test_x_getter_docstring(self):
        """x_getter Docstring Test"""
        print("test_x_getter_docstring")
        result = len(Rectangle.x.__doc__)
        self.assertTrue(result > 0, True)

    def test_y_getter_docstring(self):
        """y_getter Docstring Test"""
        print("test_y_getter_docstring")
        result = len(Rectangle.y.__doc__)
        self.assertTrue(result > 0, True)

    def test_area_docstring(self):
        """area Docstring Test"""
        print("test_area_docstring")
        result = len(Rectangle.area.__doc__)
        self.assertTrue(result > 0, True)

    def test_display_docstring(self):
        """display Docstring Test"""
        print("test_display_docstring")
        result = len(Rectangle.display.__doc__)
        self.assertTrue(result > 0, True)

    def test_str_docstring(self):
        """str Docstring Test"""
        print("test_str_docstring")
        result = len(Rectangle.__str__.__doc__)
        self.assertTrue(result > 0, True)

    def test_update_docstring(self):
        """update Docstring Test"""
        print("test_update_docstring")
        result = len(Rectangle.update.__doc__)
        self.assertTrue(result > 0, True)

    def test_to_dictionary_docstring(self):
        """to_dictionary Docstring Test"""
        print("test_to_dictionary_docstring")
        result = len(Rectangle.to_dictionary.__doc__)
        self.assertTrue(result > 0, True)

    def test_pep8_conformance(self):
        """load_from_file Docstring Test"""
        print("test_test_pep8_conformance")
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)
