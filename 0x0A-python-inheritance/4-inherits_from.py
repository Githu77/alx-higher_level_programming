#!/usr/bin/python3

"""Defines inherited function"""


def inherits_from(obj, a_class):
    """Checks if object is of inherited class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
