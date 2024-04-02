#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ele = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ele += 1
        except IndexError:
            raise IndexError("list index out of range")
        except (ValueError, TypeError):
            continue
    print()
    return (ele)
