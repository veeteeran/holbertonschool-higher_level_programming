#!/usr/bin/python3
"""
Low memory cost project
"""


class LockedClass:
    """Prevents user form dynamically creating new instance attributes

        Parameter:
            value: first_name
    """

    __slots__ = ['first_name']

    def __init__(self, value=""):
        self.first_name = value
