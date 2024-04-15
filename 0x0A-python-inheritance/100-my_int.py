#!/usr/bin/python3
"""
module contain:
class inherits from Int
"""


class MyInt(int):
    """
    class inherits from Int
    """
    def __eq__(self, other):
        """
        override equality operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        override inequality operator
        """
        return super().__eq__(other)
