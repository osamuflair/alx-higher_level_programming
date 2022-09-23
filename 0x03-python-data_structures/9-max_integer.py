#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    elif len(my_list) == 1:
        return my_list[0]
    i = 0
    while (i < len(my_list)):
        if my_list[0] > my_list[1]:
            my_list.pop(1)
        else:
            my_list.pop(0)
        i += 1
    return my_list[0]
