#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_str_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 50,
            'M' : 100
            }
    integer_result = 0
    if roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1 and roman_str_dict[roman_string[i]] < roman_str_dict[roman_string[i + 1]]:
            integer_result -= roman_str_dict[roman_string[i]]
        else:
            integer_result += roman_str_dict[roman_string[i]]
    return integer_result
