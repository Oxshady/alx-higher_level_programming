#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    for item in my_list:
        print("{}".format(int(my_list[i])))
        i += 1
