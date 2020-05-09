#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) != str or None:
        return 0

    result = 0
    length = len(roman_string)
    for i in range(length):
        num = roman.get(roman_string[i])
        if i + 1 < length and roman.get(roman_string[i + 1]) > num:
            result -= num
        else:
            result += num

    return result
