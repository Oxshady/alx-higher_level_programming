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
    that raises an Exception with the message area() is not implemented
    Public instance method: def integer_validator(self, name, value):
    that validates value
    """
    def area(self):
        """
        raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
