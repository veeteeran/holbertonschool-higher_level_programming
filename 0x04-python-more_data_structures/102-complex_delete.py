#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    dict_copy = a_dictionary.copy()
    for k, v in dict_copy.items():
        if v == value:
            a_dictionary.pop(k)

    return a_dictionary
