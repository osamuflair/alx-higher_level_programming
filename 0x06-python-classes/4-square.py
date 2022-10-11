#!/usr/bin/python3
"""
A python file to demonstrate class and object
"""


class Square:
    """
    A python class that has a value
    """
    def __init__(self, __size=0):
        self.set_x(__size)

    def set_x(self, __size):
        if type(__size) != int:
            raise TypeError("size must be an integer")
        self.__size = __size
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def get_x(self):
        return self.__size

    def area(self):
        return (self.__size)**2
