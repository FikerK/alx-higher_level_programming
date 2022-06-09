#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda X: x * x), i)) for i in matrix]
