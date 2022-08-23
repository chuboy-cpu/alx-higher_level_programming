#!/usr/bin/python3
for alpha in range(122, 96, -1):
    char = chr(alpha)
    if (alpha % 2 == 1):
        char = chr(alpha - (ord('a') - ord('A')))
        print("{}".format(char), end="")
