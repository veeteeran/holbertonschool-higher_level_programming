#!/usr/bin/python3
def max_integer(my_list=[]):
    
    max_int = 0
    if (my_list):
        for i in my_list:
            if (i > max_int):
                max_int = i
        return (max_int)
    return (None)
