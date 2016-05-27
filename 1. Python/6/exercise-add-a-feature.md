# Exercise: Add a Feature

## Objective

Add a new feature to an existing, complex codebase.

Now that you’ve fixed some bugs in the dungeon game, you should have an idea of how it’s structured. It’s time to level up by adding a new feature!

1. Download `advanced-dungeon-needs-feature.zip` (attached) to your code folder
1. Use the feature request below as your guide to implement the feature

------

## New Feature: Ring of Invisibility

Currently, the only way to win at Dungeon of Doom! is to kill the spider with the dagger. We want to offer a way to win the game without resorting to violence. The way we’re going to do this is to put a ring of invisibility in the game.

The ring should:

- Be found in the bedroom (room 3, 1 in the grid)
- Require the user to first pick it up, then put it on in a second command (so, `pu` followed at any point by `po`)
- Respond to `i_am_a` with `ring`
- Respond to `emoji` with 💍

When the player is wearing the ring:

- The player should be able to move around the room with the spider without the spider noticing them

Adding the ring will require:

- Updates to the `handle_action` and `help` methods of the `Player` class
- The addition of a `put_on` method and a `visibility` property to the `Player` class
- Updates to the `attack` method of the `Spider` class
- Updates to the `rooms_setup` function in `main.py`
