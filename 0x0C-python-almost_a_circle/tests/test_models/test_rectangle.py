#!/usr/bin/python3
"""
test for rectangle class
"""

from models.rectangle import Rectangle
import unittest


class RectangleTest(unittest.TestCase):
    """
    test for rectangle class
    """
    def setUp(self):
        """
        set up
        """
        self.r1 = Rectangle(10, 20, 2, 3, 50)
        self.r2 = Rectangle(20, 30, 3, 3)
        self.r3 = Rectangle(20, 30)

    def tearDown(self):
        """
        tear down
        """
        self.r1 = None
        self.r2 = None
        self.r3 = None

    def test_id(self):
        """
        test with and without id
        """
        self.assertEqual(self.r1.id, 50)
        self.assertEqual(self.r2.id, 1)
        self.assertEqual(self.r3.id, 2)

    def test_width(self):
        """
        test width
        """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 20)
        self.assertEqual(self.r3.width, 20)
        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_height(self):
        """
        test height
        """
        self.assertEqual(self.r1.height, 20)
        self.assertEqual(self.r2.height, 30)
        self.assertEqual(self.r3.height, 30)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10)

    def test_x(self):
        """
        test x
        """
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.x, 0)

    def test_y(self):
        """
        test y
        """
        self.assertEqual(self.r1.y, 3)
        self.assertEqual(self.r2.y, 3)
        self.assertEqual(self.r3.y, 0)

    def test_exception(self):
        """
        test exception
        """
        with self.assertRaises(TypeError):
            r4 = Rectangle("10", 10, 20, 20)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, "10", 20, 20)
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 10, 20,  20)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-1, 10, 20, 20)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, -1, 20, 20)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 0, 20, 20)
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 10, -1, 2)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-1, 10, 20, -20)

    def test_area(self):
        """
        test area
        """
        self.assertEqual(self.r1.area(), 200)
        self.assertEqual(self.r2.area(), 600)
        self.assertEqual(self.r3.area(), 600)

    def test_str(self):
        """
        test str
        """
        self.assertEqual(self.r1.str(),"[Rectangle] (<{self.id}>) <{self.x}>/<{self.y}> - <{self.width}>/<{self.height}>")

    def test_update(self):
        """
        test update
        """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update(89, 2, 3, 4, 5, 6)
