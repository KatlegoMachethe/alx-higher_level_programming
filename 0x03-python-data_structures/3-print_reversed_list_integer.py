#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function prints integers in reverse order

    Args:
        my_list: List to print in reverse.
    
    Returns:
        The elements of the list in revers
    """
    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))
    return
