#!/usr/bin/python3
"""Docstring for class_to_json"""


def class_to_json(obj):

    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

        Parameter:
            obj: instance of a Class
    """
    return obj.__dict__
