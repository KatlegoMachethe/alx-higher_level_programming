#!/usr/bin/python3

"""Module 10-student.

This Module has a class Student
which defines a student by first_name,
last_name and age

Attributes:
    firs_name (str): name of student.
    last_name (str): surname.
    age (int): Age of student.
"""

class Student():
    """Class of 2022"""

    def __init__(self, first_name, last_name, age):
        """Initializes the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary representation of instance"""
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
