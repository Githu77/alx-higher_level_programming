#!/usr/bin/python3

"""Defines inherited list."""


class MyList(list):
    """Implements list class"""

    def print_sorted(self):
        """Print in ascending order."""
        print(sorted(self))
