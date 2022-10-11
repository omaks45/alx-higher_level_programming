#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        mod = a / b
    except (TypeError, ZeroDivisionError):
        mod = None
    finally:
        print("Inside result: {}".format(mod))
    return (mod)
