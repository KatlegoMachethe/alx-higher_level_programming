#!/usr/bin/python3

"""
Module 3-say_my_name
returns my name
"""

def say_my_name(first_name, last_name=""):
    """
    Function prints the imput name
    and surname.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
    return
