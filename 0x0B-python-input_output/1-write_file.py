#!/usr/bin/python3
"""
module contain:
function that write to a text file
"""


def write_file(filename="", text=""):
    """
    function that write to a text file
    """
    with open(filename, 'w', encoding="UTF-8") as file:
        chars = file.write(text)
    return (chars)
