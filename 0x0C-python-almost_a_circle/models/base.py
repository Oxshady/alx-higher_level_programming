#!/usr/bin/python3
"""
contain base class
"""

import unittest
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

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
