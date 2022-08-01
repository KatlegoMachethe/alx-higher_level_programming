#!/usr/bin/python3

"""
Module 11-square

Inherits from Rectangle in
9-rectangle and instantiates size
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Inherits from Rectangle

    methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """instantiates size"""

        super().integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def __str__(self):
        """prints the following"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
