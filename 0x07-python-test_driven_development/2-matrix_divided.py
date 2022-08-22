#!/usr/bin/python3

"""
Module 2-matrix_divided
Does element wise matrix operations
"""

def matrix_divided(matrix, div):
    """
    This functions devides all elements of matrix
    by the dix
    """
    
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(error1)
        if len(rows) != len(matrix[0]):
            raise TypeError(error2)

        new_rows = []
        for col in rows:
            if not isinstance(col, (int, float)):
                raise TypeError(error1)
            new_rows.append(round(col / div, 2))

        new_matrix.append(new_rows)

    return(new_matrix)
