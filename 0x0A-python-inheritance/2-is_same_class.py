#!/usr/bin/python3

"""Defines function to check class"""


def is_same_class(obj, a_class):
    """Check if object is in class"""
    if type(obj) == a_class:
        return True
    return False
