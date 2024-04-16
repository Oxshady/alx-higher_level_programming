#!/usr/bin/python3
"""
module contain:
function that read a text file
"""


def read_file(filename=""):
    """
    function that read a text file
    """
    with open(filename, 'r', encoding="UTF-8") as file:
        for line in file:
            print(line)
