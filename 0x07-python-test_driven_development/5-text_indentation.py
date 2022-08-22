#!/usr/bin/python3

"""
Module 5-text_indentation
Inputs a string
Prints 2 new lines after ".", "?" and ":".
"""

def text_indentation(text):
    """
    Indents a string after characters . ? :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    new_lines = [lines.strip(' ') for lines in text.split('\n')]
    listed = "\n".join(new_lines)
    print(listed, end="")

    return
