#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)
    if lenght == 0:
        return None
    max = my_list[0]
    for x in range(0, lenght):
        if max < my_list[x]:
            max = my_list[x]
    return max
