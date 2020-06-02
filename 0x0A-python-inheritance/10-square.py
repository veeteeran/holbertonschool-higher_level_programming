#!/usr/bin/python3
"""Class Square inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """
        Init method for Square

            Parameter:
                size: size of sides of Square object
        """
        self.__width = size
        self.__height = size
        self.__size = size
        self.integer_validator = ("size", self.__size)

    def area(self):
        """Return area of Square object"""
        return self.__size ** 2

    def __str__(self):
        """Print description of Square"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
