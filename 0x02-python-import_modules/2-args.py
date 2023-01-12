#!/usr/bin/python3

import sys
x = len(sys.argv) - 1
print("{} argument".format(x), end="")
if x == 0:
    print("s.")
else:
    if x > 1:
        print("s", end="")
    print(":")
    for y in range(1, x + 1):
        print("{}: {}".format(y, sys.argv[y]))
