#!/usr/bin/python3
"""
text_indentation() prints text with two newlines after characters in list
"""


def text_indentation(text):
    """
    prints text with two newlines after characters in list

        Parameter:
            text: A string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    start = 0
    end = 0
    for char in text:
        end += 1
        if char in characters:
            print(text[start:end])
            print()
            start = end + 1
