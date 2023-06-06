#!/usr/bin/python3
for x in range(10):
    for n in range(10):
        if x == 8 and n == 9:
            print("{}{}".format(x, n))
        elif x != n and n > x:
            print("{}{}, ".format(x, n), end="")
