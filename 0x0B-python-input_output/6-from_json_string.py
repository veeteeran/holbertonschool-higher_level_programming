#!/usr/bin/python3
"""Docstring for from_json_string"""


def from_json_string(my_str):
    import json
    """
    Returns an object (Python data structure) represented
    by a JSON string

        Parameter:
            my_str: JSON string
    """
    return json.loads(my_str)
