#!/usr/bin/python3

"""
Module 2-is_same_class
Checks if object is an instance of a class
Returns True if it is and False otherwise
"""

def is_same_class(obj, a_class):
    """
    Returns boolean value
    """

    if type(obj) == a_class:
        return True
    else:
        return False
