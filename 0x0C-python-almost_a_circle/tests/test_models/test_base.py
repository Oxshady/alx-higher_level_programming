#!/usr/bin/python3
"""
test for base class
"""


import unittest
from models.base import Base


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
