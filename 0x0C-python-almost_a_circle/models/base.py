#!/usr/bin/python3
"""
contain base class
"""

import unittest
import json
import os
import turtle
import csv

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
    @classmethod
    def load_from_file(cls):
        """
        deserialization
        """
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_objs = cls.from_json_string(json.load(f))

        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to file in CSV format
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            for obj in list_objs:
                if isinstance(obj, cls):
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])


    @classmethod
    def load_from_file_csv(cls):
        """
        load from file in CSV format
        """
        filename = "{}.csv".format(cls.__name__)
        if not os.path.exists(filename):
            return []

        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)

            list_objs = []
            for row in reader:
                if len(row) == 4:
                    if cls.__name__ == "Rectangle":
                        list_objs.append(Rectangle(*map(int, row)))
                    elif len(row) == 4:
                        if cls.__name__ == "Square":
                            list_objs.append(Square(*map(int, row)))
                    else:
                        raise ValueError("Invalid format for {}".format(cls.__name__))
            return list_objs
    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """
        draw all the Rectangles and Squares
        """
        window = turtle.Screen()
        window.setup(800, 600)

        window.bgcolor("white")

        window.title("Drawing")

        for rect in list_rectangles:
            rect.draw(window)

        for square in list_squares:
            square.draw(window)
        window.mainloop()
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
