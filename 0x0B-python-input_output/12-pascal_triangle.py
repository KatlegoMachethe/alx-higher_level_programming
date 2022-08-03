#!/usr/bin/python3

"""
Modules 12-pascal_triangle.

Making Pascal's triangle from scratch.
"""

def pascal_triangle(n):
    """Returns Pascal's triangle as a list of integers
    for each n'th row.
    """
    if n <= 0:
        return []

    first = [[1]]
    while len(first) != n:
        triangle = first[-1]
        new = [1]
        for i in range(len(triangle) - 1):
            new.append(triangle[i] + triangle[i + 1])
        new.append(1)
        first.append(new)
    return first
