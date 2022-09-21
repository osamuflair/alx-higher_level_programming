#!/usr/bin/python3
def uppercase(str):
    j = len(str)
    i = 0

    while (i < j):
        if (ord(str[i]) >= 97) and (ord(str[i]) <= 122):
            shit = ord(str[i])
            mess = shit - 32
            piss = chr(mess)
        else:
            piss = str[i]
        print("{}".format(piss), end="")
        i += 1
    print("{}".format(""))
