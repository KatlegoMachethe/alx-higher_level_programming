#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """This function replaces and element in a list

    Args:
        my_list: input list
        idx: index (int) to replace
        element: new element to put in my_list

    Returns:
        The new list.
    """
    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
