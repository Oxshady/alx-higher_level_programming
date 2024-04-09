#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""


class Rectangle:
    """
    Rectangle class:
        Private instance attribute: width:
            property def width(self): to retrieve it
            property setter def width(self, value): to set it:
            width must be an integer, otherwise raise a TypeError
            exception with the message width must be an integer
            if width is less than 0, raise a ValueError
            exception with the message width must be >= 0
        Private instance attribute: height:
            property def height(self): to retrieve it
            property setter def height(self, value): to set it:
            height must be an integer, otherwise raise a
            TypeError exception with the message height must be an integer
            if height is less than 0, raise a ValueError
            exception with the message height must be >= 0
        Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
        Public instance method: def area(self): that returns the rectangle area
        Public instance method: def perimeter(self): that returns the rectangle perimeter:
            if width or height is equal to 0, perimeter has to be equal to 0
        print() and str() should print the rectangle with the character #:
            if width or height is equal to 0, return an empty string
        repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
        Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
        Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
            rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
            rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
            Returns rect_1 if both have the same area value
        Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

