#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or int
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100,	"D":500, "M":1000}
    sum ,i = 0, 0
    if len(roman_string) == 1:
        return roman[roman_string]
    else:
        while i < len(roman_string):
            r_1 = roman[roman_string[i]]
            print(r_1)
            if i != len(roman_string) - 1:
                r_2 = roman[roman_string[i + 1]]
            else:
                r_2 = 0
            print(r_2)
            if r_2 > r_1:
                sum += r_2 - r_1
                i += 2
            else:
                sum += r_1
                i += 1

    return sum