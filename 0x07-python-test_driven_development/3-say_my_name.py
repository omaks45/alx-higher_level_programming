#!/usr/bin/python3
"""A module that prints first and last name."""


def say_my_name(first_name, last_name=""):

    """This is a function that prints first and last name of a person.
    Args:
       first_name - first argument that displays a person's first name
       second_name - second argument that displays a person's second name.
    Raise:
       TypeError ("first name or second name must be a string")

    """

    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
