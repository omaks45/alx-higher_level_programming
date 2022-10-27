#!/usr/bin/python3
"""A module that defines class student"""


def __init__(self, first_name, last_name, age):
    """initialization of class student"""

    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self):
        """Retrieving dictionary representation of the student"""
        return self.__dict__
