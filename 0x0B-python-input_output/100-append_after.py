#!/usr/bin/python3
"""Docstring for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a
    specific string

        Parameters:
            filename: name of file
            search_string: insert after this string
            new_string: string to insert
    """
    with open(filename, 'r', encoding='utf-8') as f:
        my_list = list(f)

    for i in range(len(my_list)):
        if search_string in my_list[i]:
            my_list.insert(i + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as nf:
        nf.writelines(my_list)

    return filename
