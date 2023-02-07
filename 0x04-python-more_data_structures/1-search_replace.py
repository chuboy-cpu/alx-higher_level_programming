#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    return (newlist.append(x) if x != search else newlist.append(replace) for x in my_list)
