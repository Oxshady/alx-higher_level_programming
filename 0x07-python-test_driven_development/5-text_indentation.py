#!/usr/bin/python3
"""
module that contain -
function that prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print the text with 2 new lines after each '.', '?', and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    start_of_line = True
    for char in text:
        if char == ' ' and start_of_line:
            continue
        print(char, end='')
        if char in punctuation_marks:
            print('\n\n', end='')
            start_of_line = True
        elif char == '\n':
            start_of_line = True
        else:
            start_of_line = False
