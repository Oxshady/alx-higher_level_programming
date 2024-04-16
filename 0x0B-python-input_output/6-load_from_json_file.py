#!/usr/bin/python3
"""
module contain
function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    """
    with open(filename, 'r') as file:
        file_data = file.read()
        return (json.loads(file_data))
