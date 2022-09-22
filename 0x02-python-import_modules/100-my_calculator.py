#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num = len(sys.argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            exit(0)
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            exit(0)
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            exit(0)
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
