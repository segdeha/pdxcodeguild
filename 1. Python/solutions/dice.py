#!/usr/bin/env python
"""PDX Code Guild Curriculum. Dice example."""

__author__ = "Christopher Jones"
__copyright__ = "Copyright 2016, PDX Code Guild"
__version__ = "0.1"

from random import randint


def roll_dice(number_of_dice, number_of_sides):
    for die in range(1, number_of_dice + 1):
        random_integer = randint(1, number_of_sides)
        print("Die number " + str(die) + ": " + str(random_integer))

dice_number = int(input("How many dice would you like to roll? "))
dice_sides = int(input("How many sides should each die have? "))

roll_dice(dice_number, dice_sides)
