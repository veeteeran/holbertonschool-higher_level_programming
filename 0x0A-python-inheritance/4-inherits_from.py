#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class, otherwise False

        Parameters:
            obj: the object to check
            a_class: check if inherited from this class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
