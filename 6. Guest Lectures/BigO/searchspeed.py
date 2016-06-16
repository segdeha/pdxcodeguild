#!/usr/bin/env python3

from functools import partial
from random    import randint, choice

import heapq

def isorted(iterable):
    lst = list(iterable)
    heapq.heapify(lst)
    pop = heapq.heappop
    while lst:
        yield pop(lst)

def setup(size):
    newint = partial(randint, 0)
    li     = isorted((newint(size) for _ in range(size)))
    target = li[(-size // 4) + newint(size//4)]
    return li, target


def find_N(target, li):
    for index, elm in enumerate(li):
        if elm == target:
            return index
    return None


def find_logN(target, li):
    low, high = 0, len(li)

    def bisect(low, high):
        return (high + low) // 2

    while True:
        index = bisect(low, high)
        if target == li[index]:
            return index

        low, high = low, index-1 if target < li[index] else index+1, high


sample     = 100000000
li, target = setup(sample)
n_index    = find_N(target, li)
logn_index = find_logN(target, li)


