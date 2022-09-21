#!/usr/bin/python3
for e in range(ord('a'), ord('z') + 1):
    if (chr(e) != 'e' and chr(e) != 'q'):
        print('{:c}'.format(e), end="")
