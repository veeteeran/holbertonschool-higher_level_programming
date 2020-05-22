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
    in_string = False
    for char in text:
        if not char.isspace():
            in_string = True
        end += 1
        if char == " " and not in_string:
            start += 1

        if char in characters:
            print(text[start:end])
            print()
            in_string = False
            start = end
    print(text[start:end], end="")
