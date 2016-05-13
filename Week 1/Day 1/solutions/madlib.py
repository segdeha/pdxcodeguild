#!/usr/bin/env python
"""
PDX Code Guild Curriculum. Mad lib example.
This is meant to show students what a Mad lib is.
"""

__author__ = "Christopher Jones"
__copyright__ = "Copyright 2016, PDX Code Guild"
__version__ = "0.1"

print(
    'A noun is a word (other than a pronoun) used to identify any of a class of people, places, or things common noun,'
    ' or to name a particular one of these proper noun.'
)
one = input("Enter a plural noun: ")
print()
print(
    'A place is a particular position or point in space'
)
two = input("Enter a place: ")
print()
print(
    'A noun is a word (other than a pronoun) used to identify any of a class of people, places, or things common noun,'
    ' or to name a particular one of these proper noun.'
)
three = input("Enter a noun: ")
print()
print(
    'A noun is a word (other than a pronoun) used to identify any of a class of people, places, or things common noun,'
    ' or to name a particular one of these proper noun.'
)
four = input("Enter a plural noun: ")
print()
print(
    'A noun is a word (other than a pronoun) used to identify any of a class of people, places, or things common noun,'
    ' or to name a particular one of these proper noun.'
)
five = input("Enter a noun: ")
print()
print(
    'An adjective is a word or phrase naming an attribute, added to or grammatically related to a noun to modify or '
    'describe it.'
)
six = input("Enter an adjective: ")
print()
print(
    'A verb is a word used to describe an action, state, or occurrence, and forming the main part of the predicate of a'
    ' sentence, such as hear, become, happen.'
)
seven = input("Enter a verb: ")
print()
eight = input("Enter a number: ")
print()
print(
    'An adjective is a word or phrase naming an attribute, added to or grammatically related to a noun to modify or '
    'describe it.'
)
nine = input("Enter an adjective: ")
print()
print("A body part is... a part of your body")
ten = input("Enter a body part: ")
print()
print(
    'A verb is a word used to describe an action, state, or occurrence, and forming the main part of the predicate of a'
    ' sentence, such as hear, become, happen.'
)
eleven = input("Enter a verb: ")
print()
print()

print('''
Two {one}, both alike in dignity,
In fair {two}, where we lay our scene,
From ancient {three} break to new mutiny,
Where civil blood makes civil hands unclean.
From forth the fatal loins of these two foes
A pair of star-cross`d {four} take their life;
Whole misadventured piteous overthrows
Do with their {five} bury their parents` strife.
The fearful passage of their {six} love,
And the continuance of their parents` rage,
Which, but their children`s end, nought could {seven},
Is now the {eight} hours` traffic of our stage;
The which if you with {nine} {ten} attend,
What here shall {eleven}, our toil shall strive to mend.
'''.format(
    one=one,
    two=two,
    three=three,
    four=four,
    five=five,
    six=six,
    seven=seven,
    eight=eight,
    nine=nine,
    ten=ten,
    eleven=eleven
))
