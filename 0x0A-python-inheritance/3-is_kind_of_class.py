#!/usr/bin/python3

"""
Module 3-is_kind_of_class
Checks if an object is an instance of class or
class that inherited fromthe special case
Return True if it is and False otherwise
"""

def is_kind_of_class(obj, a_class):
    """
    Returns bollean value
    """

    if isinstance(obj, a_class):
        return True
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
