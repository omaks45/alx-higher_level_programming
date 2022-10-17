#!/usr/bin/python3
"""A module that divides all element of a matrix and returns a new matrix"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix by a given number.
    Args:
       matrix - contains a list numbres of rows and columns to be divided
       div - is the divisor of the rows and column of the matrix
    Returns:
       a new matrix
    Raise:
       TypeError: if the content of the matrix is not a number
       TypeError: if the row and column of the matrix are not of same size
       TypeError: if the div is not a number(neither int nor float)
       ZeroDivisionError: if the div is 0.
    """
    for (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
