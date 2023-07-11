#!/usr/bin/python3

"""Defines python class to a JSON function"""


def class_to_json(obj):
    """Return representation of data structure"""
    return obj.__dict__
