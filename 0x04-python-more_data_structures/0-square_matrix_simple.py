#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lis = list()
    for i in range(len(matrix)):
        lis += [[x**2 for x in matrix[i]]]
    return lis
