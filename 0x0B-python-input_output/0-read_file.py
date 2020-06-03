#!/usr/bin/python3
"""Docstring for read_file"""


def read_file(filename=""):
    """Reads a text file (UTF8), prints it to stdout

        Parameter:
            filename: file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
