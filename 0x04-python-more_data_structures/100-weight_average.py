#!/usr/bin/python3
def weight_average(my_list=[]):

    l1 = []
    l2 = []
    n1 = 0
    n2 = 0

    if my_list:
        for i in my_list:
            l1.append(i[0])
            l2.append(i[1])

        for a, b in zip(l1, l2):
            n1 += a * b
            n2 += b

        return n1 / n2

    return 0
