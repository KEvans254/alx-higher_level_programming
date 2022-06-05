#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for num in arr:
            if num == arr[-1]:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end = " ")
