#!/usr/bin/env python3
def no_c(my_string):
    n = len(my_string)
    i = 0
    while i < n:
        if my_string[i] == 'c':
            my_string = my_string[:i] + my_string[i + 1:]
            n -= 1
        if my_string[i] == 'C':
            my_string = my_string[:i] + my_string[i + 1:]
            n -= 1
    return my_string
