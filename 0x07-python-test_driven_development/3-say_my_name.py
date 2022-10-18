#!/usr/bin/python3
'''
a function that
prints my name
firs name and sue name
'''
def say_my_name(first_name, last_name=""):
    if first_name:
        if isinstance(first_name, str) is True:
            if isinstance(last_name, str) is True:
                print("My name is", first_name, last_name)
            else:
                raise TypeError("last_name must be a string")
        else:
            raise TypeError("first_name must be a string")
    else:
        raise TypeError("first_name must be a string")

