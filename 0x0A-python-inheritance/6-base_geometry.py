#!/usr/bin/python3
"""
module contain class BaseGeometry that contain
Public instance method: def area(self):
that raises an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """
    contain class BaseGeometry that contain
    Public instance method: def area(self):
    that raises an Exception with the message area() is not implemented    """
    def area(self):
        """
        raise exception
        """
        raise Exception("area() is not implemented")
