#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
    finally:
        if result is not None:
            print("Inside result: {:0.1f}".format(result))
        else:
            print("Inside result: {}".format(result))
    return (result)
