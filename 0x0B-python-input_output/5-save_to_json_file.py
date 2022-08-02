#!/usr/bin/python3

"""Module 5-save_to_json_file.

Writes an object to a text file as JSON.
Return: None
"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file as JSON.

    Args:
        my_obj (object): object to put in file.
        filename (str): file to write object in.
    Returns:
        Number of characters writen in filename.
    """

    with open(filename, mode="w") as f:
        return json.dump(my_obj, f)
