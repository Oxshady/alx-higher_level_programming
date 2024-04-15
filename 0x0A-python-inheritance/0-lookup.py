#!/usr/bin/python3
"""
this module contain function that
returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object
cd 
    Parameters:
    obj : object to return it's attributes and methods
    """
    return (dir(obj))
