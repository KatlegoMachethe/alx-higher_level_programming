#!/usr/bin/python3

"""Module 3-to_json_string.

The funtiion in this file the JSON
representation of an object.
"""
import json

def to_json_string(my_obj):
    """Function converts input to a json string.

    Args:
        my_obj (object): input object to make json string.
    
    Returns:
        JSON representation of the object.
    """

    return json.dumps(my_obj)
