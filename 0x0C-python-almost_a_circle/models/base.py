#!/usr/bin/python3
"""
Module base
Has the class Base which is the base
of all other classes in the project
"""


class Base:
    """
    Base class for all project classes.
    It manages "id" attributes in other classes
    to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor: Assigns class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
