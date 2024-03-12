#!/usr/bin/python3
for x in range(100):
    if x != 99:
        print("{:d}".format(x).zfill(2), end=", ")
    else:
        print("{:d}".format(x).zfill(2))