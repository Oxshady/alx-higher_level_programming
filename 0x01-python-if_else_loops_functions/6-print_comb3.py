#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x == y:
            continue
        if y > x:
            if x == 8:
                print("{:d}{:d}".format(x, y))
            else: 
                print("{:d}{:d}".format(x, y), end=", ")
