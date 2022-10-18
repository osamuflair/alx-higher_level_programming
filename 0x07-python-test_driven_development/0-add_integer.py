#!/usr/bin/python3
'''
a module that 
returns the sum
of two numbers.
'''
def add_integer(a, b=98):
    '''
    returns a + b
    '''
    if not a:
        raise TypeError("a must be an integer")
    if isinstance(a, int) is True or isinstance(a, float) is True:
        if isinstance(b, int) is True or isinstance(b, float) is True:
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
