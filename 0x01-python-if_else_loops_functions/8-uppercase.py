#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str) >= 65 and ord(str) <= 95:
            i = chr(ord(i))
        print("{}".format(i), end="")
