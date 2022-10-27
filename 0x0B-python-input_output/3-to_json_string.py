#!/usr/bin/python3
"""A module that defines a string to JSON function"""


import json


def to_json_string(my_obj):
    """json representation of an object string"""
    return json.dumps(my_obj)
