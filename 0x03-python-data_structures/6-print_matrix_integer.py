#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = 0
    for i in matrix:
        for ii in i:
            if len(i) - 1 != x:
                print("{:d}".format(ii), end=" ")
            else:
                print("{:d}".format(ii), end="")
            x += 1
        print("{}".format("\n"), end="")
        x = 0
