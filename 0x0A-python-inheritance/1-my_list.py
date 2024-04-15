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
        new = sorted(self)
        print(new)
        del (new)
