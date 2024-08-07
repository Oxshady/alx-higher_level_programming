#!/usr/bin/python3
"""
this module contain function that
-
print hi my name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints hi my name is <first name> <last name>

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except NameError:
        raise NameError("enter correct value")
