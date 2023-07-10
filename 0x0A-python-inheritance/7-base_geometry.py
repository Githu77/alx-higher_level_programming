#!/usr/bin/python3
"""Defines a base class"""


class BaseGeometry:
    """Representative"""

    def area(self):
        """unimplemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
