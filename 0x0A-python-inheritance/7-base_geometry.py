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
