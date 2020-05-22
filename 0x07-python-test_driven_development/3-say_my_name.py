#!/usr/bin/python3
"""
say_my_name() prints My name is <first_name> (optional) <last_name>
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first_name> (optional) <last_name>

        Parameters:
            first_name: A string
            last_name: A string or empty
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
