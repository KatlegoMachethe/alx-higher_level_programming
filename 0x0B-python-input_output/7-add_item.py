#!/usr/bin/python3

"""Module 7-add_item.

Adds all arguments to a python list
Returns: nothing
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(my_list=[]):
    """Adds arguments to a python list."""

    for i in sys.argv:
        my_list.append(sys.argv[i])

    with open("add_item.json", "r+") as f:
        f.write(save_to_json_file(my_list, f))

    return load_from_json_file("add_item.json")
