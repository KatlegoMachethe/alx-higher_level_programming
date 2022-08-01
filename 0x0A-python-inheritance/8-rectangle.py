#!/usr/bin/python3

"""
Module 8-rectangle

Class inhetits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Class Rectangle in the house

    methods:
        __init__(self, width, height)
    """

    def __init__(self, width, height):
        """Sets width and height"""

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

