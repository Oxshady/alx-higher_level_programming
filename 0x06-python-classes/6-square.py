#!/usr/bin/python3
""""
these module contain :-
class Square that defines a square by:
Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise
a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception
with the message size must be >= 0
Public instance method: def area(self): that returns the current square area
"""


class Square:
    """
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (len(position) != 2):
            raise IndexError("position must be a tuple of 2 positive integers")
        if (type(position[0]) is not int or type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = tuple(position)

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        """"
        function that set the size private att
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """"
        function that set the size private att
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """"
        function that set the size private att
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """"
        function that set the size private att
        """
        if (len(value) != 2):
            raise IndexError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = tuple(value)

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
