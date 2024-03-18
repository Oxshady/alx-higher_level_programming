#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        lenght = len(my_list)
        for index in range(lenght, 0, -1):
            print("{:d}".format(my_list[index - 1]))
