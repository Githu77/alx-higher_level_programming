#!/usr/bin/python3
"""prevents creating dynamic attributes"""


class LockedClass():
    """Class preventing creation of dynamic attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """Initialize method"""
        pass
