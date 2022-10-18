#!/usr/bin/python3
"""A module that prints a square with the character #"""


def print_square(size):

    """This is a function that prints a square with the character #
    Args:
       size: Represents the length of the square

    Raise:
       TypeError: if size is not an integer
       TypeError: if size is float and size less than zero
       ValueErro: if size is less than zero.

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise ValueError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
