#!/usr/bin/env python3

"""
fibonacci problem recursive and iterative
"""

def recfib(n):
    if n == 1 or n == 0:
        return n
    return recfib(n - 1) + recfib(n - 2)

def iterfib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

