#!/usr/bin/python3

"""
Module 6-base_geometry

Class raises an exeption
"""

class BaseGeometry:

    """
    Class raises an exception with message
    area() is not implemented
    
    methods:
        area(self)
    """

    def area(self):
        """Raises exception"""

        raise Exception("area() is not implemented") 
