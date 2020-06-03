#!/usr/bin/python3
"""Docstring for save_to_json_file"""


def save_to_json_file(my_obj, filename):
    import json
    """
    Write an Object to a text file, using a JSON representation

        Parameters:
            my_obj: object to save
            filename: name of text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
