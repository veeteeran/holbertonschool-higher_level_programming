#!/usr/bin/python3
"""Creates a Square object"""


class Square:
    """Creates a Square object"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes data

        Args:
            size (int): size of square
            position (tuple): position of square

        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.size = size
        if type(position) != tuple or len(position) != 2 \
                or position[0] < 0 or position[1] < 0 or \
                type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = position

    @property
    def size(self):
        """getter method size for Square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method size with type and value check for Square

        Args:
            value: size of the square
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter method property for Square object"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method property with type check"""
        if type(value) != tuple or len(value) != 2 or value[0] < 0 \
                or value[1] < 0 or type(value[0]) != int or type(value[1]) \
                != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of Square object

        Returns:
            Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints out Square using hashes(#)"""
        if (self.__size == 0):
            print()
        else:
            for newline in range(self.__position[1]):
                print()
            for row in range(self.__size):
                print("{}".format(" " * self.__position[0]), end='')
                print("{}".format("#" * self.__size, end=''))
