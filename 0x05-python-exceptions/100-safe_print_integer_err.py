#!/usr/bin/bash
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception:", e)
        return False
    else:
        return True
