#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = a_dictionary.copy()
    for i, v in b.items():
        b[i] = v * 2
    return b
