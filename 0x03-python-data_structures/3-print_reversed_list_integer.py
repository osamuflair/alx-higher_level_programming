#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for n in range(len(my_list)):
        if len(my_list) == 0:
            print("")
            break
        print("{:d}".format(my_list[-i]))
        i += 1
