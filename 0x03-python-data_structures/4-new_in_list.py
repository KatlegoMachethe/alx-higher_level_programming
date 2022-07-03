#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces element in list without modifying the original

    Args:
        my_list: input list
        idx: index in list to replace
        element: element to put in new list.

    Returns:
        replaces elements.
    """
    tmp = my_list.copy()

    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        tmp[idx] = element
        return (tmp)
