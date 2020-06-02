#!/usr/bin/python3
"""Class for base geometry"""


class BaseGeometry:
    """Class for base geometry"""
    def area(self):
        """
        Unimplemented area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates an integer

            Parameters:
                name: a string
                value: an int
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Class for Rectangle inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class for Rectangle inherits from BaseGeometry"""
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

    def area(self):
        """Return area of Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """Print description of Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

"""Class Square inherits from Rectangle"""


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size):
        """
        Init method for Square

            Parameter:
                size: size of sides of Square object
        """
        self.__size = size
        self.integer_validator = ("size", self.__size)

    def area(self):
        """Return area of Square object"""
        return self.__size ** 2

    def __str__(self):
        """Print description of Square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
