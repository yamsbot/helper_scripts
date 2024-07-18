#!/usr/bin/python3
import sys

# DEFINES
bad_char = False
bytestr = ""
count = 0
bad = 0

# COLORS
red = "\033[91m"
grn = "\033[92m"
reg = "\033[00m"

# MAIN
if __name__ == "__main__":
    if sys.argv[1] == "":
        sys.exit()

    if sys.argv[2] != "":
        bad_char = True

    with open(sys.argv[1], "rb") as f:
        while(byte := f.read(1)):
            count += 1
            if bad_char == True and byte.hex() == sys.argv[2]:
                bytestr += red + "\\x" + byte.hex() + reg
                bad += 1
            else:
                bytestr += grn + "\\x" + byte.hex() + reg
        f.close()

    print(f"bytes: {count}\nbad b: {bad}\n{bytestr}")
