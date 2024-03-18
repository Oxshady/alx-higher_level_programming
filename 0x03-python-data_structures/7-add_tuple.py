#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenght1 = len(tuple_a)
    lenght2 = len(tuple_b)

    if lenght1 >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    elif lenght1 == 1:
        a1 = tuple_a[0]
        a2 = 0
    elif lenght1 == 0:
        a1 = 0
        a2 = 0
    if lenght2 >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    elif lenght2 == 1:
        b1 = tuple_b[0]
        b2 = 0
    elif lenght2 == 0:
        b1 = 0
        b2 = 0
    new = (a1 + b1, a2 + b2)
    return (new)
