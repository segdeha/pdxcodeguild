#!/usr/bin/env python

"""
This is a program to help users think about computational complexity.
This is a real whiteboard interview coding problem.

Given a string and a collection of strings, can you construct the base
string using elements from your collection?
"""

n = int()

def is_constructable(word, parts):
    """
    Is 'word' constructable from elements of 'parts'?
    """
    if not word:
        return True

    for i, _ in enumerate(word, 1):

        global n
        n += 1 # assumes that O(1) lookup of 'word' in 'parts'

        if word[:i] in parts:
            if is_constructable(word[i:], parts):
                return True

    return False


def most_substrings(s):
    """
    creates complete collection of substrings
    """
    for i, _ in enumerate(s):
        for j, _ in enumerate(s, 1):
            word = s[i:j]
            if word:
                yield word


class opstr(str):
    def __new__(cls, *args, **kw):
        global n
        n = 0
        return str.__new__(cls, *args, **kw)

    def __str__(self):
        global n
        return '{!r} {!r}'.format(len(self), n)


for wump in ('hi', 'yup', 'them', 'grape', 'catdog', 'oranges'):
    word = opstr(wump)

    is_constructable(word, set(most_substrings(word[:-1])))
    print(word)

