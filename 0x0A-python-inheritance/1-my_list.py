#!/usr/bin/python3
"""A class that inherits from list"""


class MyList(list):
    """Inherits from list """
    def print_sorted(self):
        """
        Prints the list, in ascending order
        """
        if type(self) is not list or self == []:
            return
        new_list = self[:]
        new_list.sort()
        return print(new_list)
