#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n1= 0
    n2 = 0
    for tup in my_list:
        n1 += tupl[0] * tupl[1]
        n2 += tupl[1]

    return (n1/ n2)
