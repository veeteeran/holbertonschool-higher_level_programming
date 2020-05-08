#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = dict(I=1, IV=4, V=5, X=10, XL=40, L=50,
                XC=90, C=100, CD=400, D=500, CM=900, M=1000)

    if type(roman_string) != str or None:
        return 0

    result = 0
    if roman_string:
        for i in roman_string:
            result += roman[i]

    return result
