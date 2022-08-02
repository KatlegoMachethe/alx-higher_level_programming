#!/usr/bin/python3

"""Module 3-to_json_string.

The funtiion in this file the JSON
representation of an object.
"""
import json

def from_json_string(my_str):
    """Function converts json string to python DS.

    Args:
        my_str (object): input object to make json string.
    
    Returns:
        Python object representation of JSON string.
    """

    return json.loads(my_str)
