#!/usr/bin/python3
"""A module that prints first and last name."""


def say_my_name(first_name, last_name=""):

    """This is a function that prints name (<first name> <last name>)
    Args:
       first_name(str) - first name to be printed
       second_name(str) - second name to be printed.

    Raise:
       TypeError ("first name or second name must be a string")

    """

    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")

    print(f"My name is {first_name}, {last_name}")
