#!/usr/bin/python3
"""A module that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """print a sorted list"""

        print(sorted(self))
