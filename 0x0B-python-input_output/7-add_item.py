#!/usr/bin/python3

"""Module 7-add_item.

Adds all arguments to a python list
Returns: nothing
"""

from sys import argv
import os.path

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend(argv[1:])
    save_to_json_file(my_list, "add_item.json")
