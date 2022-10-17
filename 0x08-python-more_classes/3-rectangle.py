#!/usr/bin/python3
'''
a python class
'''


class Rectangle:
    '''
    that has value
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return 0
        for m in range(self.__height):
            for n in range(self.__width):
                str1 += "#"
            if m != self.height - 1:
                str1 += "\n"
        return str1
