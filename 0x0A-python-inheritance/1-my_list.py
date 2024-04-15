#!/usr/bin/python3
"""
this module contain:
class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """sort list then print it"""
        print(sorted(self))
