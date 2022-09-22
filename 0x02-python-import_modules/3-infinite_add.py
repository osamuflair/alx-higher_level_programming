#!/usr/bin/python3
import sys
if __name__ == "__main__":
    length = len(sys.argv)
    i = 1
    total = 0
    while (i < length):
        total += int(sys.argv[i])
        i += 1
    print(total)
