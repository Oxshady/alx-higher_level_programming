#!/usr/bin/python3
def uppercase(str):
    if ord("a") <= ord(str) <= ord("z"):
        print ("{:c}".format((ord(str) - 32)))
uppercase("s")