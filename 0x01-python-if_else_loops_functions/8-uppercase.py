#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str) >= 97 and ord(str) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
