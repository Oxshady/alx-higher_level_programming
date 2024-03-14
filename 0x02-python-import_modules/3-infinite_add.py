#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{:d}".format(0))
    else:
        sum = 0
        counter = 0
        for number in argv:
            counter += 1
            if counter == 1:
                continue
            sum += int(argv[counter - 1])
    if len(argv) > 1:
    	print("{:d}".format(sum))
