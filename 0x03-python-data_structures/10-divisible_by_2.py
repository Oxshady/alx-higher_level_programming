#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    LENGHT = len(my_list)
    lis = [0] * LENGHT
    for i in range(0, LENGHT):
        if my_list[i] % 2 == 0:
            lis[i] = True
        else:
            lis[i] = False
    return (lis)
