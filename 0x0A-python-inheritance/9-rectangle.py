#!/usr/bin/python3

"""
Module 9-rectangle

Class that inherits from BaseGeormetry
in module 7-base_geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ 
    Class of Rectangle

    methods:
        __init__(self, width, height)
        area(self)
    """

    def __init__(self, width, height):
        """instentiate width and height"""

        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
