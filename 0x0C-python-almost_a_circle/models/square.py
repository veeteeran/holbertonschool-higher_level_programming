#!/usr/bin/python3
"""Docstring for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Init method for square
        
            Parameters:
                size: size of sides of square
                x: x position
                y: position
                id: id of object
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overload of __str__ method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                   self.x, self.y, self.__size)

    @property
    def size(self):
        """getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method with type and value check

            Parameter:
                value: size of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each Square attribute"""
        my_list = [None, None, None, None]

        for i in range(len(args)):
            my_list[i] = args[i]

        if my_list[0] != None:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if my_list[1] != None:
            self.__size = args[1]
        elif 'size' in kwargs:
            self.__size = kwargs['size']
        if my_list[2] != None:
            self.x = args[2]
        elif 'x' in kwargs:
            self.x = kwargs['x']
        if my_list[3] != None:
            self.y = args[3]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        new_dict = {}
        for key in self.__dict__.keys():
             if 'size' in key:
                 new_dict['size'] = self.__dict__[key]
             elif 'x' in key:
                 new_dict['x'] = self.__dict__[key]
             elif 'y' in key:
                 new_dict['y'] = self.__dict__[key]
             elif 'id' in key:
                 new_dict['id'] = self.__dict__[key]
        return new_dict
