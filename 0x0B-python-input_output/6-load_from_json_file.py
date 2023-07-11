#!/usr/bin/python3

"""Defines a function to read file in JSON"""
import json


def load_from_json_file(filename):
    """Create python object from JSON file"""
    with open(filename) as f:
        return json.load(f)
