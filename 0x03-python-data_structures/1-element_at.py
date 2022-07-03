#!/usr/bin/python3
def element_at(my_list, idx):
    """Funtions that retries an element from a list

    Args:
        my_list: input list.
        idx: 1st integer
    Returns:
        None when idx < 0.
        None when idx > len(my_list)
    """
    if idx < 0 or idx > len(my_list):
        return ("None")
    else:
        return (my_list[idx])
