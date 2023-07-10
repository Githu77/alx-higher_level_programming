#!/usr/bin/python3

"""Defines a class and function"""


def is_kind_of_class(obj, a_class):
    """Check if object is in class"""
    if isinstance(obj, a_class):
        return True
    return False
