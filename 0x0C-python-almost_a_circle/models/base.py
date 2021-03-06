#!/usr/bin/python3
"""Docstring for Base class"""
import json
import csv


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
        if list_dictionaries is None or list_dictionaries == []:
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
            if list_objs is None and type(list_objs) is not list:
                f.write("[]")
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())

                new_str = cls.to_json_string(new_list)
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
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation of list_objs
           to a csv file

            Parameter:
                list_objs: a list of instances that inherits from Base
        """
        new_list = []
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            fieldnames = ['width', 'height', 'x', 'y', 'id']
        elif cls.__name__ == "Square":
            fieldnames = ['size', 'x', 'y', 'id']

        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None and type(list_objs) is not list:
                f.write("[]")
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())

                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for d in new_list:
                    writer.writerow(d)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances
        """
        my_list = []
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    for value in r:
                        r[value] = int(r[value])
                    obj = cls.create(**r)
                    my_list.append(obj)

                return my_list
        except:
            return []
