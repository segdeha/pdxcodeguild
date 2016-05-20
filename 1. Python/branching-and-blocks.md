# Branching & Blocks

Programs need to make decisions to do the work we want the to.
`if` statements let us selectively execute code paths.

    if is_raining:
      wear_jacket = True
      mood = 'sad'
    else:
      wear_jacket = False
      mood = 'happy'
    wear_shoes = True
    wear_pants = True

An `if` statement takes a _Boolean expression_ and only executes a following **block** if the expression is `True`.

## Blocks

A block is a group of statements to be run together in order.
All statements in a block are indented four spaces more than before.

Indentation is important! **Only use 4 spaces.** Double check that your editor is actually inserting spaces and not tabs. Atom has “Toggle Invisibles” which shows dots wherever you have spaces and double chevrons wherever you have tabs.

There are two blocks in the above example:

    wear_jacket = True
    mood = 'sad'

and

    wear_jacket = False
    mood = 'happy'

Blank lines have nothing to do with whether code is included in a block. The following is identical to above:

    if is_raining:
      wear_jacket = True
    
      mood = 'sad'
    else:
      wear_jacket = False
      mood = 'happy'
    
    wear_shoes = True
    wear_pants = True

Blocks can be **nested**. Just indent four more spaces.

    if is_raining:
      if is_warm:
        wear_jacket = False
      else:
        wear_jacket = True
      mood = 'sad'

Blocks only come after a colon, `:`. If you see a colon, you need an indented block on the next line, and vice versa.

## Structure of `if` Statements

An if statement is made up of one `if` **branch**, zero or more `elif` branches, and zero or one `else` branch. Each `if` and `elif` branch evaluates a Boolean expression.

The Boolean expressions are evaluated from _top to bottom_ and the first one to evaluate to `True` is executed. If none evaluate to `True`, the `else` branch is run. _Only one_ branch is run.

    if num_legs < 2:
      print('snake')
    elif num_legs < 3:
      print('human')
    elif num_legs < 5:
      print('dog')
    else:
      print('octopus')

In this example, only one animal will be printed.
