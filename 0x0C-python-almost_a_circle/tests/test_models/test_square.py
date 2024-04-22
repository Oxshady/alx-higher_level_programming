#!/usr/bin/python3
"""
test for square class
"""


from models.square import Square
import unittest

class TestSquare(unittest.TestCase):
    """
    test for square class
    """
    def setUp(self):
        self.square = Square(5)
    def test_id(self):
        """
        test class with and without id
        """
        s1 = Square(20)
        s2 = Square()
        s3 = Square()
        s4 = Square(-2)
        s5 = Square(14.1)
        s6 = Square()
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s4.id, 4)
        self.assertEqual(s5.id, 5)
        self.assertEqual(s6.id, 6)
        self.assertEqual(type(s1.id), int)
        self.assertEqual(type(s2.id), int)
        self.assertEqual(type(s3.id), int)
        self.assertEqual(type(s4.id), int)
        self.assertEqual(type(s5.id), int)
    def test_update_with_positional_args(self):
        self.square.update(1, 2, 3, 4)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.size, 2)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 4)

    def test_update_with_kwargs(self):
        self.square.update(id=10, size=15, x=20, y=25)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 15)
        self.assertEqual(self.square.x, 20)
        self.assertEqual(self.square.y, 25)

    def test_update_with_invalid_args(self):
        with self.assertRaises(ValueError):
            self.square.update(1, 2, 3, 4, 5)

    def test_update_with_invalid_kwargs(self):
        with self.assertRaises(ValueError):
            self.square.update(id=10, size=15, x=20, y=25, z=25)
