#!/usr/bin/python3
class Square:
    def __str__(self):
        return "{'_Square__size':", self.__size, +"}"
    def __init__(self, __size):
        self.__size = __size
