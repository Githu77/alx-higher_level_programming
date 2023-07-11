#!/usr/bin/python3

"""Defines JSON function to write files."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to file in JSON."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
