#!/usr/bin/python3
def roman_to_int(roman_string):
    c = 0
    d = len(roman_string)
    if roman_string is None or roman_string == "":
        return c
    if not isinstance(roman_string, str):
        return c
    else:
        for i in range(len(roman_string)):
            if roman_string[i] == 'I':
                if d == i + 1 or roman_string[i + 1] == 'I':
                    c += 1
                else:
                    c -= 1
                continue
            elif i == 'V':
                c += 5
                continue
            elif i == 'X':
                if d == i + 1 or roman_string[i + 1] == 'X' or roman_string[i + 1] == 'V' or roman_string[i + 1] == 'I':
                    c += 10
                else:
                    c -= 10
                continue
            elif i == 'L':
                c += 50
                continue
            elif i == 'C':
                if d == i + 1 or roman_string[i + 1] == 'X' or roman_string[i + 1] == 'V' or roman_string[i + 1] == 'I' or roman_string[i + 1] == 'C':
                    c += 100
                else:
                    c -= 100
                continue
            elif i == 'D':
                c += 500
                continue
            elif i == 'M':
                if d == i + 1 or roman_string[i + 1] == 'X' or roman_string[i + 1] == 'V' or roman_string[i + 1] == 'I' or roman_string[i + 1] == 'C' or roman_string[i + 1] == 'M':
                    c += 1000
                else:
                    c -= 1000
                continue
    return c


