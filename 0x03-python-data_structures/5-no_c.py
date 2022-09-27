#!/usr/bin/python3

def no_c(my_string):
    new_str = ''
    for e in my_string:
        if e != 'c' and e != 'C':
            updated_str += e
    return (new_str)
