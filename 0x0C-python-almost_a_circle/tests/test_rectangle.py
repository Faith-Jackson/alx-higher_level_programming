#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 262
    TestRectangle_y - line 334
    TestRectangle_order_of_initialization - line 402
    TestRectangle_area - line 430
    TestRectangle_update_args - line 538
    TestRectangle_update_kwargs - line 676
    TestRectangle_to_dictionary - line 788
"""
import io
import sys
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor_with_valid_values(self):
        rect = Rectangle(10, 20, 5, 8, 1)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 8)
        self.assertEqual(rect.id, 1)

    def test_constructor_with_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 8, 1)

    def test_constructor_with_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(10, -5, 5, 8, 1)

    def test_constructor_with_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 8, 1)

    def test_constructor_with_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -8, 1)

    def test_constructor_with_invalid_id(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, 8, "not_an_integer")

    def test_area_calculation(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.area(), 20)

    def test_display_method(self):
        rect = Rectangle(3, 2)
        with self.assertOutput(stdout="###\n###\n"):
            rect.display()

    def test_update_method_with_args(self):
        rect = Rectangle(4, 5, 1, 2, 3)
        rect.update(7, 8, 9, 10, 11)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 11)

    def test_update_method_with_kwargs(self):
        rect = Rectangle(4, 5, 1, 2, 3)
        rect.update(id=7, width=8, height=9, x=10, y=11)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 9)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 11)

    def test_to_dictionary_method(self):
        rect = Rectangle(4, 5, 1, 2, 3)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {'id': 3, 'width': 4, 'height': 5, 'x': 1, 'y': 2})

    def test_str_representation(self):
        rect = Rectangle(4, 5, 1, 2, 3)
        self.assertEqual(str(rect), "[Rectangle] (3) 1/2 - 4/5")

if __name__ == '__main__':
    unittest.main()

