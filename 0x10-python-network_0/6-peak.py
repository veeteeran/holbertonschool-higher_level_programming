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
    for i in range(len(list_of_integers)):
        if i == 0:
            bigboi = list_of_integers[i]
        elif list_of_integers[i] > bigboi:
            bigboi = list_of_integers[i]
    return bigboi
