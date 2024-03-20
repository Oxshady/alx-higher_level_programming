#!/usr/bin/python3
def uniq_add(my_list=[]):
    matrix = my_list
    matrix.sort()
    result = 0
    for i in range(0, len(matrix)):
        if i != 0:
            if matrix[i] == matrix[i - 1]:
                continue
        result += matrix[i]
    return (result)
