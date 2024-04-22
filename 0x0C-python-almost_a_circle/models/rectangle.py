#!/usr/bin/python3
import unittest
"""
contain rectangle class inherits from base
"""


from base import Base


class Rectangle(Base):
    """
    Rectangle class:
    inherits from Base
    attr:
    width of rect
    height of rect
    x
    y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        rectangle constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return (self.__width)

    @width.setter
    def width(self, Width):
        """
        widht setter
        """
        if type(Width) is not int:
            raise TypeError("width must be an integer")
        if Width <= 0:
            raise ValueError("width must be > 0")
        self.__width = Width

    @property
    def height(self):
        """
        height getter
        """
        return (self.__height)

    @height.setter
    def height(self, Height):
        """
        height setter
        """
        if type(Height) is not int:
            raise TypeError("height must be an integer")
        if Height <= 0:
            raise ValueError("height must be > 0")
        self.__height = Height

    @property
    def x(self):
        """
        x getter
        """
        return (self.__x)

    @x.setter
    def x(self, X):
        """
        x setter
        """
        if type(X) is not int:
            raise TypeError("x must be an integer")
        if X < 0:
            raise ValueError("x must be >= 0")
        self.__x = X

    @property
    def y(self):
        """
        y getter
        """
        return (self.__y)

    @y.setter
    def y(self, Y):
        """
        y setter
        """
        if type(Y) is not int:
            raise TypeError("y must be an integer")
        if Y < 0:
            raise ValueError("y must be >= 0")
        self.__y = Y


if __name__ == "__main__":

    r2 = Rectangle(10, 10, -2, -2)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
