#!/usr/bin/python3
"""Creates a Rectangle object"""


class Rectangle:
    """Creates a Rectangle object"""
    def __init__(self, width=0, height=0):
        """
        Initialize rectangle

            Parameters:
                width: an int
                height: an int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method with type and value check

            Parameters:
                value: width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method with type and value check

            Parameters:
                value: height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Print rectangle using #"""
        string = ""
        for row in range(self.__height):
            string += ("#" * self.__width)
            if row != self.__height - 1:
                string += "\n"

        return string
