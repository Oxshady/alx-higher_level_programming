#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("{}".format("0 arguments."))
    elif len(argv) == 2:
        print("{}".format("1 argument:"))
        print("{:d}: {}".format(len(argv) - 1, argv[len(argv) - 1]))
    else:
        print("{} argument:".format(len(argv) - 1))
        counter = 0
        for token in argv:
            counter += 1
            if counter == 1:
                continue
            else:
                print("{:d}: {}".format(counter - 1, token))
