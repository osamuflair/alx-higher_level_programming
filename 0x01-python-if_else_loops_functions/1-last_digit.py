#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = repr(number)
con = num[-1]
if number < 0:
    con = -int(con)
else:
    con = int(con)
if con > 5:
    print(f"Last digit of {number} is {con} and is greater than 5")
elif con == 0:
    print(f"Last digit of {number} is {con} and is 0")
else:
    print(f"Last digit of {number} is {con} and is less than 6 and not 0")
