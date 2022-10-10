#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        print("Inside result: {}".format(a / b))
        c = a / b
    except:
        print("Inside result: {}".format(None))
        c = None
    finally:
        return c
