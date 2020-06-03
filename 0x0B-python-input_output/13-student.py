#!/usr/bin/python3
"""Docstring for class Student"""


class Student:
    """
    Defines a student by first name, last name, age
    """
    def __init__(self, first_name, last_name, age):
        """
        Init method for Student

            Parameters:
                first_name: first name
                last_name: last name
                age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary description
        """
        if type(attrs) is list and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for k in list(self.__dict__.keys()):
                if k in attrs:
                    new_dict[k] = self.__dict__[k]
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        if 'first_name' in json:
            self.first_name = json['first_name']
        if 'last_name' in json:
            self.last_name = json['last_name']
        if 'age' in json:
            self.age = json['age']
