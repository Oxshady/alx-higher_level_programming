#!/usr/bin/python3
"""
this module contain
-
function that print a square with a character #
"""


def print_square(size):
    """
    function that print a square with a character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
