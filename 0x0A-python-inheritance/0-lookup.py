#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
        Parameter:
            obj: object passed to function
    """
    return dir(obj)
