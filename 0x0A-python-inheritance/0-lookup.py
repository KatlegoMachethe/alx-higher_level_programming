#!/usr/bin/python3
"""
Module 0-lookup
returns the list of available
attributes and methods of an object
"""

def lookup(obj):
    """
    Funtions looks for attributes and methods

    Args:
        obj (object): Attributes and methods
    Rerurns:
        list of attributes
    """
    return dir(obj)
