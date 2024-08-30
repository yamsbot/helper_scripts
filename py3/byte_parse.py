#!/usr/bin/env python3
import sys

bad_char = False
bytestr = ""
count = 0
bad = 0

red = "\033[91m"
grn = "\033[92m"
reg = "\033[00m"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    if len(sys.argv) == 3:
        bad_char = True
        bad_chars = sys.argv[2].split(",")
        print("bad", bad_chars)

    with open(sys.argv[1], "rb") as f:
        while(byte := f.read(1)):
            count += 1
            if bad_char and byte.hex() in bad_chars:
                bytestr += red + "\\x" + byte.hex() + reg
                bad += 1
            else:
                bytestr += grn + "\\x" + byte.hex() + reg
        f.close()

    print(f"bytes: {count}\nbad b: {bad}\n{bytestr}")
