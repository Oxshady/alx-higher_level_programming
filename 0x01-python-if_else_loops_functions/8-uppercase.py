#!/usr/bin/python3
def uppercase(str):
    if len(str) > 1:
        for x in str:
            if ord("a") <= ord(x) <= ord("z"):
                print("{:c}".format((ord(x) - 32)),end="")
    else:
        if ord("a") <= ord(x) <= ord("z"):
            print("{:c}".format((ord(x) - 32)),end="")
    print("")
