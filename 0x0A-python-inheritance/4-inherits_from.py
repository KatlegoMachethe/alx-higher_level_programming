#!/usr/bin/python3

"""
Module 4-inherits_from
Checks if an object is an instance of a class
that inherited from the special class
"""

def inherits_from(obj, a_class):
    """ Reurns a boolean value """

    return issubclass(type(obj), a_class) and type(obj) != a_class
