#!/usr/bin/python3
"""MyInt Class inherits from int"""


class MyInt(int):
    """MyInt inherits from int"""

    def __eq__(self, other):
        """
        Redefine equality to be unequal

            Parameters:
                self: instance of the object
                other: other object to compare against
        """
        if isinstance(type(other), type(self)):
            return self == other
        return False

    def __ne__(self, other):
        """
        Redefine equality to be unequal

            Parameters:
                self: instance of the object
                other: other object to compare against
        """
        return not self.__eq__(other)
