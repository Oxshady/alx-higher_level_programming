#!/usr/bin/python3
"""
module contain:
Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Instantiation with width and height.
    """
    def __init__(self, width, height):
        """
        constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        and calc the area
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
