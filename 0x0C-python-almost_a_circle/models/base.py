#!/usr/bin/python3
"""
contain base class
"""

import unittest


class Base:
    """
    base class (super class)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class TestBase(unittest.TestCase):
    """
    class that test base class
    """
    def test_id(self):
        """
        test class with and without id
        """
        base1 = Base(20)
        base2 = Base()
        base3 = Base()
        base4 = Base(-2)
        base5 = Base(14.1)
        base6 = Base()
        base7 = Base(None)
        self.assertEqual(base1.id, 20)
        self.assertEqual(base2.id, 1)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, -2)
        self.assertEqual(base5.id, 14.1)
        self.assertEqual(base6.id, 3)
        self.assertEqual(base7.id, 4)


if __name__ == "__main__":
    unittest.main()
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
