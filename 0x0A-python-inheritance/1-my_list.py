#!/usr/bin/python3

"""
Module 1-my_list
Class inheriting from listand has
a public method print_sorted that prints
the list sorted in ascending order
"""

class MyList(list):
    """
    Inherits from list

    methods:
        print_sorted(self)
    """

    def print_sorted(self):
        """
        Prints a sorted list
        """

        print(sorted(self))
