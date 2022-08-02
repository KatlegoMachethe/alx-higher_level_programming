#!/usr/bin/python3

"""Module 2-append_write

The function appends a tring at the
end of a text file
"""

def append_write(filename="", text=""):
    """This function appends a text to filename.tct

    Args:
        filename (str): text file to append to.
        text (str): Text to add to filename.
    Returns:
        Number of characters added.
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
