#!/usr/bin/python3
"""find_peak doctring"""


def find_peak(list_of_integers):
    """
    Description:
        Finds a peak in a list of unsorted integers
    Args:
        List of integers
    """
    if list_of_integers == []:
        return None
    return max(list_of_integers)
