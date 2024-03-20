#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixes = []
    for List in matrix:
        row = list(map(lambda i: i ** 2, List))
        matrixes.append(row)
    return (matrixes)
