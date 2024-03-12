#!/usr/bin/python3
char = 97
while char <= 122:
    if char != 101 and char != 113:
        print("{:c}".format(char), end="")
    char += 1
