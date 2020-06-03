#!/usr/bin/python3
"""Class for Rectangle inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for Rectangel inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Init method for Rectangle

            Parameters:
                width: width of Rectangle object
                height: height of Rectangle object
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
