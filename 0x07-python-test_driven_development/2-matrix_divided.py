#!/usr/bin/python3
'''
a script
that divides elements
of a matrix
'''
def matrix_divided(matrix, div):
    for m in range(len(matrix)):
        for n in matrix[m]:
            if type(n) not in [int, float]:
                i = "matrix must be a matrix (list of lists) of integers/floats"
                raise TypeError(i)
        if m != len(matrix) - 1:
            if len(matrix[m]) != len(matrix[m + 1]):
                raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix1 = []
    matrix2 = []
    for m in range(len(matrix)):
        for n in matrix[m]:
            matrix1.append(float("{:.2f}".format(n / div)))
        matrix2.append(matrix1.copy())
        matrix1.clear()
    return matrix2
