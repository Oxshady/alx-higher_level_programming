#!/usr/bin/python3
"""
module contain :
class Square that inherits from Rectangle:
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Instantiation with size.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        returns a string representation of the square.
        """
        return f"[Rectangle] {self._Rectangle__width}/{self._Rectangle__height}"
