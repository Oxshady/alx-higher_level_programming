#!/usr/bin/python3
x = 122
while x >= 97:
    if x % 2 == 0:
        print("{:c}".format(x), end="")
    else:
        print("{:c}".format(x - 32), end="")
    x = x - 1
