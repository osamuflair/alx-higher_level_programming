#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for n in range(list_length):
        try:
            a = my_list_1[n] / my_list_2[n]
            new_list.append(a)
        except:
            a = 0
            new_list.append(a)
    return new_list
