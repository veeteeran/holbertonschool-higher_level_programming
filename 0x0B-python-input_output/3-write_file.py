#!/usr/bin/python3
"""Docstring for write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file, UTF8,
    returns the number of characters written

        Parameters:
            filename: file written to
            text: text to write
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
