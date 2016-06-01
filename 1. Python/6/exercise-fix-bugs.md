# Exercise: Fix Bugs

## Objective

Fix two bugs in an existing, complex codebase.

1. Have one person in your pair download `advanced-dungeon-buggy.zip` (attached) to a sibling directory to your code folder (i.e. **not** inside your code folder)
1. Follow the directions [here](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/) to make this `advanced-dungeon-buggy` directory into a repo on GitHub
1. Add your fellow pair programmer to the new repo as a collaborator
1. Use the bug reports below to find and fix the defects

------

## Bug Report #1

Our first bug report comes from internal QA as you’re getting ready for a new release.

> **Summary:**
> When first running `advanced-dungeons-buggy/main.py`, some kind of console output shows up on the screen. It’s really distracting.
>
> **Observed behavior:**
> The program prints out a bunch of junk, like “Room(description=You are in a small, dank room with no windows and low ceilings.” But I haven’t even created my character yet.
>
> **Expected behavior:**
> The program shouldn’t print out a bunch of unnecessary junk to the screen.
>
> **Steps to reproduce:**
> 1. Run the program by typing `python main.py` in the terminal
> 2. Wait for it….
>
> **Other details:**
> I’m using Python 3 on OS X 10.11.4.

------

## Bug Report #2

Our second bug report comes courtesy of an upset end-user.

> **Summary:**
> There’s no way to kill the spider!!! WTF??!!
>
> **Observed behavior:**
> I have the stupid dagger, but no matter what I do I can’t kill the spider! It never gets past being ‘wounded’.
>
> **Expected behavior:**
> Attacking the spider should kill it, obviously!
>
> **Steps to reproduce:**
> 1. Start the game
> 2. Go east and get the dagger
> 3. Go north and attack the spider
> 4. No matter how much you attack, it never dies
>
> **Other details:**
> I’m never playing this game again if you don’t fix this!!!

------

## Extra Credit: Bug Report #3

Our third bug report is one a fellow developer noticed in the course of playing the game.

> **Summary:**
> Hitting `h` (help) when you’re in the room with the spider allows the spider to attack you. You shouldn’t get attacked for hitting `h`. Same for `i`, I suppose.
>
> **Observed behavior:**
> See above.
>
> **Expected behavior:**
> Hitting `h` in the spider room should be a noop. I.e. the spider shouldn’t be able to attack you.
>
> **Steps to reproduce:**
> 1. Start the game
> 2. Go north into the spider room
> 3. Hit `h` to see the list of commands
> 4. Observe that the spider successfully attacks you
>
> **Other details:**
> N/A
