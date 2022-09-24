#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for n in range(len(matrix)):
        for m in matrix[n]:
            print("{:d}".format(m), end=" ")
        print("")
