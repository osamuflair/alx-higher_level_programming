#!/usr/bin/python3
def uniq_add(my_list=[]):
    mylist = set(my_list)
    mylis = list(mylist)
    if mylis is None:
        return 0
    y = 0
    for i in mylis:
        y += i
    return y
