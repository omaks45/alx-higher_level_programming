#!/usr/bin/python3
"""A module that defines a python class to json function"""


def class_to_json(obj):
    """"dictionary description with simple data structure"""
    return obj.__dict__
