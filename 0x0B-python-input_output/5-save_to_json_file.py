#!/usr/bin/python3
"""A module that defines a json file writing"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using json representation"""
    with open(filename, 'w') as x:
        json.dump(my_obj, x)
