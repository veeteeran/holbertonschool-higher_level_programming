#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    True if the object is exactly an instance of specified class, otherwise False

        Parameters:
            obj: the object to check
            a_class: check if inherited from this class
    """
    if isinstance(obj, a_class):
        return True

    return False
