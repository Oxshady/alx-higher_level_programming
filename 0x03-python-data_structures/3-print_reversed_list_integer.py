#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new = my_list
    new.reverse()
    for i in new:
        print("{:d}".format(i))
