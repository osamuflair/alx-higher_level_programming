#!/usr/bin/python3
import functools
def uniq_add(my_list=[]):
    mylist = set(my_list)
    mylis = list(mylist)
    if mylis is None:
        return 0
    return functools.reduce(lambda x,y: x+y, mylis)
