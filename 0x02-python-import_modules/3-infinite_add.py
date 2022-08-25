#!/usr/bin/python
if __name__ == "__main__":
    import sys
    x = 0
    for y in range(1, len(sys.argv)):
        x += int(sys.argv[y])
        print("{}".format(x))
