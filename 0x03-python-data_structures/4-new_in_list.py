#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for n in my_list:
        if n - 1 == idx:
            new_list.append(element)
            continue
        new_list.append(my_list[n - 1])
    return new_list
