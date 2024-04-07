#!/usr/bin/python3
"""
addition module
there is add_integer method which add two nums
two nums must be float or int
"""


def add_integer(a, b=98):
    """
    Returns: int: the sum of a and b  a first num b second num, b default to 98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
