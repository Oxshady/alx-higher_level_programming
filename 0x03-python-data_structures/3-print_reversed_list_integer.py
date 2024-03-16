#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    x = 0
    for i in my_list:
        print("{:d}".format(my_list[x]))
        x += 1
