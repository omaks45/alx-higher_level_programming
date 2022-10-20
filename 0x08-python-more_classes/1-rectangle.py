#!/usr/bin/python3
"""A module containing a rectangle"""


class Rectangle:
    """Representation of class rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of class rectangle.
        Args:
           width - stands for the rectangle width
           height - stands for the e rectangle height.
        Raise:
           TypeError: if size is not an integer.
           ValueError: if size is less than zero.

        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """retrieve the width attribute"""
            return self.__width

        @width.setter
        def width(self, value):
            """set width attribute"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """retrieve the height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """set the height attribute"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("value must be >= 0")
            self.__height = value
