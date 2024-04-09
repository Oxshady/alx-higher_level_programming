#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except NameError:
        raise NameError("enter correct value")
if __name__ == "__main__":
    say_my_name("shadi", "mahmoud")