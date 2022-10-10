#!/usr/bin/python3
def safe_print_division(a, b):
    """returns the division of a by b."""
    try:
        mod = (a / b)
    except(ZeroDivisionError, TypeError):
        mod = none
    finally:
        print("inside result: {}".format(mod))
    return mod
