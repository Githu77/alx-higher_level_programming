#!/usr/bin/python3
"""prevents creating dynamic attributes"""


def magic_string(l=[]):
    """prevents creating dynamic attributes"""
    l += ["BestSchool"]
    return ", ".join(l)
