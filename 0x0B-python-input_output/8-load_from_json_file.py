#!/usr/bin/python3
"""Docstring for load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”

        Parameter:
            filename: JSON file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
