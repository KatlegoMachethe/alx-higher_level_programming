#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function printing an integer

    Args:
        my_list:Input list.

    Returns:
        prints all the integers of my_list.
    """
    for i in range(0, len(my_list)):
        if isinstance(my_list[i], int):
            print("{}".format(my_list[i]))
        else:
            i = i + 1
