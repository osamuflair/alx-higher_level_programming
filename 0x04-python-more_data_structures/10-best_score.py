#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    b = 0
    c = "t"
    for i, v in a_dictionary.items():
        if b > v:
            b = b
            c = c
        else:
            b = v
            c = i
    return c
