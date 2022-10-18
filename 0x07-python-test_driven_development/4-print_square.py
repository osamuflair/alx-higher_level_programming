#!/usr/bin/python3
'''
a function
that prints a square
with hash tag
'''
def print_square(size):
    '''
    prints a square
    '''
    if isinstance(size, int) is True:
        if size >= 0:
            for n in range(size):
                for m in range(size):
                    print("#", end="")
                print()
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")

