#!/usr/bin/env python3
import sys

''' 
this script does simple things that make my life easier
'''

def runner(mode, string):
    i = y = 0
    output = ""

    if mode == "cs":
        output += "{ "
        for v in string:
            output += hex(ord(v)) + ", "

        output = output[:-2]
        output += ", 0x00 };"
        return output

    elif mode == "lindian":
        for v in string:
            if i % 8 == 0 and i != 0:
                output = "\n0x" + output
                y += 1
            output = hex(ord(v))[2:].zfill(2) + output
            i += 1

        if y != 0 and i % 8 == 0:
            return output
        else:
            return ("0x" + output)
    
    elif mode == "text":
        output += "{ "
        with open(string, "rb") as f:
            while(byte := f.read(1)):
                output += "0x" + byte.hex() + ", "
        f.close()
        output = output[:-2]
        output += " };"
        return output

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(runner(sys.argv[1], sys.argv[2]))
    else:
        exit()

