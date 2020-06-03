#!/usr/bin/python3
"""Docstring for to_json_string"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

        Parameter:
            my_obj: JSON obj
    """
    return json.dumps(my_obj)
