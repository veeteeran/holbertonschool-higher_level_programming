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

    def to_json(self):
        """
        Returns the dictionary description
        """
        return self.__dict__
