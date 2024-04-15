#!/usr/bin/python3
"""
module contain  function that returns True
if the object is an instance of
, or if the object is an instance
of a class that inherited from, the specified class
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object
    is an instance of, or if the object is an instance of a class
    that inherited from, the specified classotherwise False.
    """
    return (issubclass(obj, a_class))
