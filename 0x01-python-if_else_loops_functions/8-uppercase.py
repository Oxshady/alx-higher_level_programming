#!/usr/bin/python3
def uppercase(str):
    if len(str) > 0:
        for x in str:
            if ord("a") <= ord(x) <= ord("z"):
                print("{:c}".format((ord(x) - 32)),end="")
    elif len(str) == 0:
        return (0)
    print("")
