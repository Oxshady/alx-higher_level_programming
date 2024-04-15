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
        """print the list in acc ord"""
        print(sorted(self.copy()))
