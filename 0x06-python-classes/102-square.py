#!/usr/bin/python3
"""Creates a Square object"""


class Square:
    """Creates a Square object"""
    def __init__(self, size=0):
        """Initializes data"""
        self.size = size

    def area(self):
        """Returns the area of Square object"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter method for Square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method with type and value check for Square"""
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __new__(self, size):
            """Creates new instance of the same object"""
            return size

