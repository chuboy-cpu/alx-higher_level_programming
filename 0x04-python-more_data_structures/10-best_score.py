#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    x = sorted(a_dictionary.values())
    if x:
        for k in a_dictionary:
            if x[-1] == a_dictionary[k]:
                return k
    else:
        return None
