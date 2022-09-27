#!/usr/bin/python3

""" Python - Input/Output 13.Search and Update """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file
        after each line containing a
        specific string
    """
    with open(filename, "r") as f:
        i = f.readlines()

    with open(filename, "w") as f:
        for line in i:
            o.append(line)
        if search_string in line:
            o.append(new_string)
        f.write(o)
