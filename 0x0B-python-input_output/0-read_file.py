#!/usr/bin/python3
"""
Module 0-read__file

Reads file and prints to standard output.
"""

def read_file(filename=""):
    """ Function read_file
    
        This function reads a text file and prints
        it to the standars output.

        Args:
            filename (str): Name of file.
        Returns:
            nothing.
        """

    with open(filename, encoding="utf-8") as f:
        print(f.read())
