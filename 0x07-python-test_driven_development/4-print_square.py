#!/usr/bin/python3
"""
print_square() Prints square using "#"
"""


def print_square(size):
    """
    prints a square using "#"

        Parameter:
            size: An int >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        print("#" * size)
