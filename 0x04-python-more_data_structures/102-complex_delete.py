
def complex_delete(a_dictionary, value):
    for k in a_dictionary:
        if value == a_dictionary[k]:
            remove = k
    del a_dictionary[remove]
    return a_dictionary 

dict = {1:"we", 2:"do", 3:"pet", 4:"rat", 5:"pig"}

print(dict)
print(complex_delete(dict,"rat"))