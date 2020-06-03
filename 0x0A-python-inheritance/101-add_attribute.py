#!/usr/bin/python3
"""Docstring for add_attribute"""


def add_attribute(obj, name, value):
    """
    Add attribute, raise TypeError if not possible

        Parameters:
            obj: the object to add attribute
            name: attribute name
            value: value of atribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

