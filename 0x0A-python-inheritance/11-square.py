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
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Print description of Square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
