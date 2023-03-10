#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    if isinstance(roman_string, str):
        conversions_dict = {
	    'IV': 4,
	    'IX': 9,
	    'I': 1,
	    'V': 5,
	    'XL': 40,
	    'XC': 90,
	    'X': 10,
	    'L': 50,
	    'CD': 400,
	    'CM': 900,
	    'C': 100,
	    'D': 500,
	    'M': 1000 }
        while roman_string != '':
            for key in conversions_dict.keys():
                if key in roman_string:
                    integer += conversions_dict.get(key)
                    roman_string = roman_string.replace(key, '', 1)
    else:
        return 0

    return integer
