#!/usr/bin/python3
def safe_function(fct, *args):

    import sys

    try:
        return fct(args[0], args[1])
    except (ZeroDivisionError, IndexError, ValueError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
