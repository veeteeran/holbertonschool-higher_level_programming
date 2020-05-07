#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    keys = a_dictionary.keys()
    values = a_dictionary.values()
    dbl_val = [x * 2 for x in values]
    new_dict = {k:v for k, v in zip(keys, dbl_val)}

    return new_dict
