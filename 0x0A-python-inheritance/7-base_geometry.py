#!/usr/bin/python3

"""Defines base class"""


class BaseGeometry:
    """Reprsentative"""

    def area(self):
        """unimplemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate as integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
