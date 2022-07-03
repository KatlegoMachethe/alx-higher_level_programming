#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C

    Args:
        my_string: input string

    Returns:
        A new string without characters c & C.
    """
    my1 = my_string.replace('c', '')
    my2 = my1.replace('C', '')
    return (my2)
