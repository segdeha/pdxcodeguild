# Thinking Like a Programmer: Decomposition

Decomposition is the process of breaking a problem into smaller problems that, when solved and connected back together, solve the big problem.

Example:

Take the example of programming a character in a video game. You might decompose the larger task of creating the player character into parts such as movement, sound, health, attacks, inventory, etc.

You can decompose each of those into smaller parts as well. For example, movement can be broken down into direction and speed. Later, you might add collision detection so the player can’t (as an example) walk through walls.

For a simple side-scroller game, movement direction might just consist of moving left and right. Most games of this type only allow you to go back so far, so something you might implement is a limit on how far to the left the player can move.

Programming your game, you would continue in this way, breaking down problems into smaller problems, then implementing solutions to the problems until you have a working game.

## Process

1. Understand the requirements
1. Break big problems into smaller problems
1. Identify problems small enough to keep in your head at one time
1. Solve the small problems one at a time
1. Connect the dots
1. Once your program is working, refactor/improve/optimize
    - Add error/exception handling
    - Change variable/function names to be more clear and descriptive
    - Add comments (docstrings for functions, comments for tricky/non-obvious parts of the code)

Example:

- Big problem: Determine whether a given string is a palindrome

- Smaller problems:
    - Get the string from the user and store it in a variable
    - Reverse the string and store it in another variable
    - Compare the 2 strings
    - Based on the comparison results, display an answer to the user

Translate smaller problems into code:

    user_input = input('Enter a string: ')
    # reversed = <not sure off the top of my head, come back to this!>
    if user_input == reversed:
        print('It is a palindrome!')
    else:
        print('It is not a palindrome!')

Because the step of reversing the string isn’t immediately obvious, we defer it until we put together the rest of the program. This allows us now to focus on just that problem. Once we solve it, our program will be done!

A search of Google tells us that you can reverse a string by doing the following:

    'abc'[::-1]  # > 'cba'

Having quickly verified in the Python shell that this works, let’s use this as our approach. Filling in the previously commented-out line in our program above gives us the following:

    user_input = input('Enter a string: ')
    reversed = user_input[::-1]
    if user_input == reversed:
        print('It is a palindrome!')
    else:
        print('It is not a palindrome!')

This is a really simple example, but it illustrates the process you should follow for breaking big problems down into smaller ones.

------

Sources:

1. [The Beginner Programmer's guide to Problem Solving ](http://www.codeproject.com/Tips/833768/The-Beginner-Programmers-guide-to-Problem-Solving)
