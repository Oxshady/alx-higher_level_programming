#!/usr/bin/python3
"""
module contain :
class Square that inherits from Rectangle:
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle:
    """
    def __init__(self, size):
        """
        Instantiation with size.
        """
        self.integer_validator("Size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
