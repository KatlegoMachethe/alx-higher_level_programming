#!/usr/bin/python3

"""
Module 7-base_geometry

Hass class BaseGeometry
"""

class BaseGeometry:
    """
    Class of BaseGeometry

    methods:
        area(self)
        integer_validator(self, name, value)
    """

    def area(self):
        """ Raise Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
