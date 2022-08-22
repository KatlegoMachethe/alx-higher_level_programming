#!/usr/bin/python3

"""
Module 4-print_square
Prints a square using character #..
Only float and int input.
"""

def print_square(size):
    """
    Responsible for printing a square with #.
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")

    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#"*size for i in range(size)]))
    return
