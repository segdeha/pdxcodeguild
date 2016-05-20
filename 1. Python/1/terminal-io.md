# Terminal I/O

The following Python outputs nothing:

    name = 'David'
    'Hi, ' + name

We have to explicitly make values print to or read from the terminal. That is the only way to interface with the users of your program!

This is called **input/output** or **I/O.** Python gives us two functions to do that.

`print` prints an expression to the terminal as a string.

    print(value)

`input` waits for typing on the keyboard and returns the string of what was typed when [enter] is pressed.

    input()

Just calling `input` on it’s own will throw away the value from the keyboard. You have to assign the value into a variable to save it for later.

    name = input()
