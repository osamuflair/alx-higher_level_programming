#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        num = number * -1
    else:
        num = number
    while (num > 9):
        num = num % 10
    print("{}".format(num), end="")
    return num
