#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    a = my_list[0]
    for n in my_list:
        if n >= a:
            a = n
        else:
            a = a
    return a
