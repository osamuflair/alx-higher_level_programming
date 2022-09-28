#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mylist = my_list.copy()
    m = mylist.count(search)
    if m == 0:
        return mylist
    for i in range(m):
        n  = mylist.index(search)
        mylist[n] = replace
    return mylist
