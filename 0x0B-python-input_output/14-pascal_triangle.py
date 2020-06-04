#!/usr/bin/python3
"""Docstring for pascal_triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s
    triangle of n

        Parameter:
            n: an integer
    """
    matrix = []
    if n <= 0:
        return matrix

    for i in range(1, n + 1):
        num = 1
        row = []
        for j in range(1, i + 1):
            num = int(num * (i - j) / j)
            if row == []:
                row.append(1)
            if j < i:
                row.append(num)
        matrix.append(row)
    return matrix
