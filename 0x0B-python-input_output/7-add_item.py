#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file:
"""


import sys
import json
save_module = __import__('5-save_to_json_file')
load_module = __import__('6-load_from_json_file')
save_to_json_file = save_module.save_to_json_file
load_from_json_file = load_module.load_from_json_file


def main():
    """
    script that adds all arguments to a Python list,
    and then save them to a file
    """
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    main()
