#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    remove =[]
    for k in a_dictionary:
        if value == a_dictionary[k]:
            remove.append(k)
    for i in remove:
        del a_dictionary[i]
    return a_dictionary 

dict = {1:"we", 2:"do", 3:"pet", 4:"rat", 5:"pig", 6:"rat"}

