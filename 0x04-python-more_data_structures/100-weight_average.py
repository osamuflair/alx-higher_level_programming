#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    c = 0
    j = 0
    for i in range(len(my_list)):
        c += ((my_list[i][0]) * (my_list[i][1]))
        j += my_list[i][1]
    return c / j
