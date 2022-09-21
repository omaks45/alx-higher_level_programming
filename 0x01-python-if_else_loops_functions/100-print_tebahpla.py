#!/usr/bin/python3
for e in range(ord('z'), ord('a') - 1, -1):
    if e % 2 == 0:
        cont = 0
    else:
        cont = 32
    print('{}'.format(chr(e - cont)), end='')
