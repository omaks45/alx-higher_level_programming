#!/usr/bin/python3
for e in range(0, 10):
    for i in range(e+1, 10):
        if e == "8" and i == "9":
            print("89")
        else:
            print("{}{}, ".format(e, i), end="")
