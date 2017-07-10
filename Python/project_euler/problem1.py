#!/usr/bin/python3

limit = 10
total = 0

for x in range(1,limit):
    if (x % 3 == 0) or (x % 5 == 0):
        #print(x)
        total += x

print("Total: {0}".format(total))
