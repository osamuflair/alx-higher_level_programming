#!/usr/bin/python3
'''
a function that prints a text
with 2 new lines after each
of these characters: ., ? and :
'''
def text_indentation(text):
    '''
    prints a text with two new lines after...
    '''
    if type(text) == str:
        for n in text:
            print(n, end="")
            if n == '.' or n == '?' or n == ':':
                print()
                print()
    else:
        raise TypeError("text must be a string")
