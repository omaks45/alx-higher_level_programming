#!/usr/bin/python3
"""A module that reads a text file function"""


def read_file(filename=""):
    """prints a utf-8 text file to stdout"""

    with open(filename, encoding="utf-8") as my_file:
        print(my_file(), end="")
