#!/usr/bin/python3

"""Defines function for JSON-to-object"""
import json


def from_json_string(my_str):
    """Return python object representation"""
    return json.loads(my_str)
