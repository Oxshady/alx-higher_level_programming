#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # new = my_list
    # new.reverse()
    x = 0
    # for i in new:
    #     print("{:d}".format(new[x]))
    #     x += 1
    # del (new)
    for x in my_list[::-1]:
        print("{:d}".format(x))
