#!/usr/bin/python3
def uppercase(str):
    for char in str:
        x = ord(char)
        if (ord(char) >= 97 and ord(char) <= 122):
            x -= 32
            print("{}".format(chr(x)), end ="")
            print()
