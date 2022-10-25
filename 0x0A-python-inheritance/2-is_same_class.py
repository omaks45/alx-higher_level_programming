#!/usr/bin/python3
"""A functiion that shows if an object is an instance of class"""


def is_same_class(obj, a_class):
    """returns True if object is an instance of the class
    otherwise false"""

    return (type(obj) == a_class)
