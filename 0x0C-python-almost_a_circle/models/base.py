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
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write json strings to file
        """
        if list_objs is None:
            list_objs = []
        file = "{}.json".format(cls.__name__)
        with open(file, 'w') as f:
            json.dump(cls.to_json_string(list_objs), f)
    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Base":
            return None

        if cls.__name__ == "Rectangle":
            dum = cls(1, 1, 1)
            dum.update(**dictionary)
            return dum
    
        

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
