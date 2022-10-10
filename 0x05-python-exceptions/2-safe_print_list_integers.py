#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for e in range(x):
        try:
            print("{:d}".format(my_list[e]), end="")
            total +=
        except(TypeError, ValueError):
            pass
    print()
    return (total)
