#!/usr/bin/python3
""" def roman_to_int(roman_string):
	if roman_string is None or isinstance(roman_string, (int, float)):
		return 0
	roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	sum = 0
	i = 0
	if len(roman_string) == 1:
		return roman[roman_string]
	while i < len(roman_string):
		r_1 = roman[roman_string[i]]
		if i != len(roman_string) - 1:
			r_2 = roman[roman_string[i + 1]]
		else:
			r_2 = 0
		if r_2 > r_1:
			sum += r_2 - r_1
			i += 2
		else:
			sum += r_1
			i += 1
	return sum """
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        arabic = digits[roman]
        total += arabic if total < arabic * 5 else -arabic
    return total
