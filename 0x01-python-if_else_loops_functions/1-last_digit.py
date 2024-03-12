#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num == 0:
    print(f"Last digit of {num:d} is {num:d} and is 0")
elif num > 0:
    LD = num % 10
    if LD > 5:
        print(f"Last digit of {num:d} is {LD:d} and is greater than 5")
    elif LD == 0:
        print(f"Last digit of {num:d} is {LD:d} and is 0")
    elif LD < 6 and LD != 0:
        print(f"Last digit of {num:d} is {LD:d} and is less than 6 and not 0")
elif num < 0:
    LD = abs(num) % 10
    LD *= -1
    if LD > 5:
        print(f"Last digit of {num:d} is {LD:d} and is greater than 5")
    elif LD == 0:
        print(f"Last digit of {num:d} is {LD:d} and is 0")
    elif LD < 6 and LD != 0:
        print(f"Last digit of {num:d} is {LD:d} and is less than 6 and not 0")
