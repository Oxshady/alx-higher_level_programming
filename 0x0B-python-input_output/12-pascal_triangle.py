#!/usr/bin/python3
"""
module contain
    Create a function def pascal_triangle(n):
    that returns a list of lists of integer
    s representing the Pascals triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module
"""


def pascal_triangle(n):
    """
    Create a function def pascal_triangle(n):
    that returns a list of lists of integer
    s representing the Pascals triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return (triangle)
