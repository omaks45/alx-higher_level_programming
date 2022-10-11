#!/usr/bin/python3
"""A module that defines a square."""


class Square:
    """Representation of square"""

    def __init__(self, size=0):
        """initializing the class square
        Args:
            size - represents the square size
        Raise:
            TypeError: if size is not an integer.
            ValueError: if size less than zero.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
