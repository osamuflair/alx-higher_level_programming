#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for n in my_list:
        a += 1
    try:
        for m in range(x):
            print(my_list[m], end="")
        print()
        return x
    except:
        print()
        return a
