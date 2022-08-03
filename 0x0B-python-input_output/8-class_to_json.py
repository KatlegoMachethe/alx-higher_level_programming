#!/usr/bin/python3

"""Module 8-class_to_json.

Has function returning dict description
with data structures (list, dict, str, int and bool)
for JSON serialization of an object.
"""

def class_to_json(obj):
    return obj.__dict__
