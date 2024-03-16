#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenght1 = len(tuple_a)
    lenght2 = len(tuple_b)
    if lenght1 >= 2 and lenght2 >= 2:
        new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new
    elif lenght1 < 2 and lenght2 >= 2:
        if lenght1 == 0:
            new = (0 + tuple_b[0], 0 + tuple_b[1])
        else:
            new = (tuple_a[0] + tuple_b[0], 0 + tuple_b[0])
        return new
    elif lenght2 < 2 and lenght1 >= 2:
        if lenght2 == 0:
            new = (tuple_a[0] + 0, tuple_a[1] + 0)
        else:
            new = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
        return new
