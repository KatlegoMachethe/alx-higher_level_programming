#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Replaces all occurrences of an element
    """
    if matrix:
        return [list(map(lambda j: j**2, i)) for i in matrix]n
