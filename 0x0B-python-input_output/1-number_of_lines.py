#!/usr/bin/python3
"""Docstring for number_of_lines"""


def number_of_lines(filename=""):
    """
    Returns the number of lines of a text file

        Parameter:
            filename: file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line_num = 0
        for line in f:
            line_num += 1

    return line_num
