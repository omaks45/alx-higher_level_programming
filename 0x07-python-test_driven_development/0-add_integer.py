#!/usr/bin/python3
def add_integer(a, b=98):
    """A module of function which test and returns the sum of two integers.
    Args:
         a - first argument
         b - second argument
    Return:
         an integer: the addition of a and b
    Raises:
         TypeError: a must be an integer or b must be an integer
    """

    if not isinstance(a, int) and not isinstance(b, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be and integer")
    return (int(a) + int(b))
