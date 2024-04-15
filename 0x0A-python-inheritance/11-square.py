#!/usr/bin/python3
"""
module contain :
class Square that inherits from Rectangle:
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class rect
    """
    def __init__(self, size):
        """
        constructor
        """
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        calc area
        """
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
