#!/usr/bin/python3

"""Defines rectangle and subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents square."""

    def __init__(self, size):
        """new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
