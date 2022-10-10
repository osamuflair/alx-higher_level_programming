#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for n in range(list_length):
        try:
            a = my_list_1[n] / my_list_2[n]
        except(ZeroDivisionError, TypeError, ValueError, IndexError):
            a = 0
        finally:
            new_list.append(a)
    return new_list
