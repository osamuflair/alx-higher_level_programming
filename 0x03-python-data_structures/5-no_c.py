#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for n in range(len(my_string)):
        if my_string[n] == "c" or my_string[n] == "C":
            continue
        new_string = new_string + my_string[n]
    return new_string
