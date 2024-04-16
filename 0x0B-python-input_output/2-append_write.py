#!/usr/bin/python3
"""
module contain:
function that append a string to text file
"""


def append_write(filename="", text=""):
    """
    function that append a string to text file
    """
    with open(filename, 'a', encoding="UTF-8") as file:
        chars = file.write(text)
    return (chars)
