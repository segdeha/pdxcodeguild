#!/usr/bin/env python3

"""

"""
from random  import shuffle

from .threetrees import OTree

ilist = list(range(20000000))
shuffle(ilist)
print('shuffle complete')
value = ilist[-1]
print('making set')
iset  = set(ilist)
print('making tree')
itree = OTree(ilist)

containers = {'list' : ilist, 'set' : iset, 'tree' : itree}
for key in containers:
    input('is {} in our {}?'.format(value, key))
    print(value in containers[key])

