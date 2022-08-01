#!/usr/bin/python3

"""
Module 10-square

Class inherits from Rectangle
in module 9-rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class inherits from Rectangle

    methods:
        __init__(self, size)
        area(self)
    """

    def __init__(self, size):
        """Instantiates size"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
