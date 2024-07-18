#!/usr/bin/python3
import sys

''' 
quick string to little endian for ctfs

'''

i = y = 0
output = ""

if sys.argv[1] != "":
    for v in sys.argv[1]:
        if i % 8 == 0 and i != 0:
            output = "\n0x" + output
            y += 1
        output = hex(ord(v))[2:].zfill(2) + output
        i += 1

if y != 0 and i % 8 == 0:
    print(output)
else:
    print("0x" + output)
