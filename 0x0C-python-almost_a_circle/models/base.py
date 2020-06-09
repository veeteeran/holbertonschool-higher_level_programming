#!/usr/bin/python3
"""Docstring for Base class"""
import json


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method for Base class

            Parameter:
                id: an id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
           list_dictionaries

            Parameter:
                list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs
           to a file

            Parameter:
                list_objs: a list of instances that inherits from Base
        """
        my_str = ""
        new_list = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())

                new_str = (cls.to_json_string(new_list))
                f.write(new_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        json_string

            Parameter:
                json_string: string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

            Parameter:
                dictionary: Can be thought of as a double pointer to
                a dictionary
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        my_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                my_dict = cls.from_json_string(f.read())

            for d in my_dict:
                obj = cls.create(**d)
                my_list.append(obj)

            return my_list
        except:
            return []

    def __del__(self):
        """Detect when object deleted"""

        if Base.__nb_objects <= 0:
            Base.__nb_objects = 0
        else:
            Base.__nb_objects -= 1
