#!/usr/bin/python3
def uppercase(str):
    for char in str:
        x = char
        if ord(char) >= 97 and ord(char) <= 122:
            x = chr(ord(char) - (ord('a') - ord('A')))
            print("{}".format(x), end ="")
            print()
