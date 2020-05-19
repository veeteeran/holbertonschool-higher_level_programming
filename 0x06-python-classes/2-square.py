#!/usr/bin/python3
"""Creates a square object"""


class Square:
    """Creates a Square object"""
    def __init__(self, size=0):
        """Initializes data, checks for proper type and input"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
