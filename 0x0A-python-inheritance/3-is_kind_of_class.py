#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class
    otherwise False

        Parameters:
            obj: the object to check
            a_class: the class to compare against
    """
    if isinstance(obj, a_class) or issubclass(type(obj), type(a_class)):
        return True

    return False
