#!/usr/bin/python3

"""Module 6-load_from_json_file.

Creates object from a JSON file.
Return: None
"""

import json

def load_from_json_file(filename):
    """Creates an object from a JSON file."""

    with open(filename, "r") as f:
        returnjson.load(f)
