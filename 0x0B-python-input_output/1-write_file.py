#!/usr/bin/python3

"""
Module 1-write_file

Writes a string to a text file
"""

def write_file(filename="", text=""):
    """Function to to write string to text

    Args:
        filename (str): file to write to.
        text (str): text to write into file.
    Returns:
        Number of characters written.
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
