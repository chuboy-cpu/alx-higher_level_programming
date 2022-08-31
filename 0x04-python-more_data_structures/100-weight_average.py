#!/usr/bin/python3
def weight_average(my_list=[]:
        if my_list == []:
            return 0
        size = 0
        average = 0
        for tpl in my_list:
            average += (tpl[0] * tpl[1])
            size += tpl[1]
        return average/size

