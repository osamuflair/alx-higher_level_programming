#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(length - 1))
    if length > 1:
        i = 1
        while (i < length):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
