#!/usr/bin/python3
"""
Divided each element in the matrix by div
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix

        Parameters:
            matrix: a list of lists, can contain ints or floats
            div: a non-zero int

        Returns:
            a new matrix, each element divided by div
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise TypeError("division by zero")

    size_err = "Each row of the matrix must have the same size"
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_msg)
    count = 0
    current_len = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_msg)
        if count == 0:
            current_len = len(row)
        else:
            prev_len = current_len
            current_len = len(row)
            if prev_len != current_len:
                raise TypeError(size_err)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(err_msg)
        count += 1

    result = list(map(lambda x:
                      list(map(lambda i: round(i / div, 2), x)), matrix))

    return result
