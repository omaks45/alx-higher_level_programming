#!/usr/bin/python3
"""A module that writes a string to a file"""


def write_file(filename="", text=""):
    """Writes a string to a utf-8 text file"""
    with open(filename, 'w', encoding="utf-8") as x:
        return x.write(text)
