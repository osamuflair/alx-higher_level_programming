#!/usr/bin/python3
for i in range(10):
    for j in range(i,10):
        if i == j or i == 89:
            continue
        print("{}{},".format(i, j), end=" ")
print(89)
