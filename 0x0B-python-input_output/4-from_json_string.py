#!/usr/bin/python3
"""A module that defines a json to object function"""


import json


def from_json_string(my_str):
    """An object represented by a JSON string"""
    return json.loads(my_str)
