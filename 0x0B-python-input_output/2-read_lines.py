#!/usr/bin/python3
"""Docstring for read_lines"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines of a text file (UTF8), prints to stdout

        Parameters:
            filename: file to read
            nb_lines: Lines to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line_num = 0
        for line in f:
            if nb_lines <= 0:
                print(line, end="")
            elif line_num < nb_lines:
                print(line, end="")

            line_num += 1
