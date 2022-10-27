#!/usr/bin/python3
"""A module that defines a json file reading function"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename) as x:
        return json.load(x)
