#!/usr/bin/python3
"""Docstring for append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added

        Parameters:
            filename: file to append
            text: text to append to file
    """
    with open(filename, 'a+', encoding='utf-8') as f:
        return f.write(text)
