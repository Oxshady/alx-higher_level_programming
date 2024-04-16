#!/usr/bin/python3
"""
    converts an instance of a class to a dictionary
"""


def class_to_json(obj):
    """
    converts an instance of a class to a dictionary
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        # Exclude methods and attributes starting with '__'
        if not callable(value) and not key.startswith("__"):
            json_dict[key] = value
    return json_dict
