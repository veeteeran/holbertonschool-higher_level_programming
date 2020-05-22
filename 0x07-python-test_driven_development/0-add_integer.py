#!/usr/bin/python3
"""
add_integer returns a + b
"""


def add_integer(a, b=98):
    """
    Casts floats to int and with valid input returns a + b

        Parameters:
            a (int): A decimal integer
            b (int) Another decimal integer

        Returns:
            a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
