#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update(key = value)
    for i, v in a_dictionary.items():
        print("{:s}: {}".format(i, v))
