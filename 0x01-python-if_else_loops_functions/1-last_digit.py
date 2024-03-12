#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number == 0:
    print(f"Last digit of {number:d} is {number:d} and is 0")
elif number > 0:
    LD = number % 10
    if LD > 5:
        print(f"Last digit of {number:d} is {LD:d} and is greater than 5")
    elif LD == 0:
        print(f"Last digit of {number:d} is {LD:d} and is 0")
    elif LD < 6 and LD != 0:
        quote = "and is less than 6 and not 0"
        print(f"Last digit of {number:d} is {LD:d} and {quote}")
elif number < 0:
    LD = abs(number) % 10
    LD *= -1
    if LD > 5:
        print(f"Last digit of {number:d} is {LD:d} and is greater than 5")
    elif LD == 0:
        print(f"Last digit of {number:d} is {LD:d} and is 0")
    elif LD < 6 and LD != 0:
        quote = "and is less than 6 and not 0"
        print(f"Last digit of {number:d} is {LD:d} and {quote}")
