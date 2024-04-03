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
    def __init__(self, size=0) -> None:
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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

    def my_print(self):
        if self.size is not 0:
            for i in range(self.size):
                for ii in range(self.size):
                    print("#", end="")
                print()
        else:
            print()
