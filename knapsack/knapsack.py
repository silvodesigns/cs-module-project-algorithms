#!/usr/bin/python

import sys
import os
from collections import namedtuple

arg = sys.argv

# Item = namedtuple('Item', ['index', 'size', 'value'])
d = {}
with open('data/' + arg[1]) as r:
    for x in r:
        x = x.split()
        a = x[0]
        b = x[1]
        c = x[2]
        d[int(a)] = int(b), int(c)


# print(d)
# sorted_d = sorted(d.items(), key=lambda x: x[1][1], reverse=True)
# print(sorted_d[0][1][0])
# print(d)
# print(sorted_d)
# for i in sorted_d:
#     print(i[0], i[1])
# for x in a_item._asdict().items():
#     print(x)


def knapsack_solver(items, capacity):
    limit = int(capacity)
    cart = 0
    bag = []
    sorted_d = sorted(items.items(), key=lambda x: x[1][1], reverse=True)
    for x in sorted_d:
        value = x[1][1]
        cart += value
        if cart <= limit:
            bag.append(x)
        else:
            cart -= value

    # print(bag)
    # print(cart)


knapsack_solver(d, arg[2])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')

# Goal :
#  maximizing the value of a set of items you select
#  that are constrained by total size/weight

#  Take input file with following formating:
#      C  V
#    1 42 81
#    2 42 42
#    3 68 56
#    4 68 25
#    5 77 14

#    cost to put item in bagpack: 42
#    value of chosen item: 81

# The goal is to select a subset of the items to maximize the payoff such that the cost is below some threshold e.g

#   `python knapsack.py input.txt 100`

# 1 come up with something
#  Ask some questions?
#  1- What the limit of size or value I can contain in the bag?
#  2- How can I read input from command line in python ?
#  3- How can I read data from txt files in Python ?
#  4- How can I convert that data in objects in Python ?
#  5- How can I sort these set of values to pick items that yield higher value ?
