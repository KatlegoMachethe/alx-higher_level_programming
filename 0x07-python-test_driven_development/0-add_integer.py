#!/usr/bin/python3
"""
Module 0-add_integer
Has function that adds the a and b of type int/float
Returns the sum
"""

def add_integer(a, b=98):
    """This function takes a (int) and b (int)
    Return: a + b as integer.
    """

    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
