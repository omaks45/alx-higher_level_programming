#!/usr/bin/python3
"""A module that appends a string to a file"""


def append_write(filename="", text=""):
    """appending a string to a utf-8 text file"""
    with open(filename, 'a', encoding="utf-8") as x:
        return x.write(text)
