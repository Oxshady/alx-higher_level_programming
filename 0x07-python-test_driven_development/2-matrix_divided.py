#!/usr/bin/python3
"""
this module contain function that
-
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    if div should not be 0
    return new matrix
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if matrix is not None:
        matrix2 = []
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            lenght = len(matrix[0])
            if lenght != len(row):
                raise TypeError("Each row of the matrix must have the same size")
            new_row = []
            for item in row:
                if not isinstance(item,(float, int)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                new_row.append(round(item / div, 2))
            matrix2.append(new_row)
    return(matrix2)