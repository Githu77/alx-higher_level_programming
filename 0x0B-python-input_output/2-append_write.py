#!/usr/bin/python3

"""Defines function to append file"""


def append_write(filename="", text=""):
    """adds string to end of UTF8 file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
