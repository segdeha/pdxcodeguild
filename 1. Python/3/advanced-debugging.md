# Advanced Debugging

In [basic debugging](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/basic-debugging.md), we learned to listen to the errors given to you by the interpreter and to double-check out mental model when we don’t get the result we expect.

As your programs become more complicated, it can be helpful to use more robust debugging tools to understand the state of your program.

You can run your program from within PyCharm, enabling you to stop the program’s execution and inspect the values of variables at any time. You can also step through the program, line by line.

Let’s try it out!

1. Launch PyCharm
1. Open your code folder
1. Set your default debug configuration to point to Python 3
1. Open `dice.py`
1. Click in gutter next to the line with our `print` statement
1. Right-click on the name of the file and choose “Debug 'dice'” (or type ctrl-shift-d)
1. Click into the console and enter a number of dice and a number of sides per die

PyCharm should stop at the `print` statement and show you the current state of the environment, including the values for our variables `die`, `number_of_dice`, and `number_of_sides`.

From here, you can do the following:

- Resume the program (run until the next breakpoint)
- Step over — execute the current line and stop at the next line in our program
- Step into — dive into any function calls within the current line
- Step out — climb back up the callstack (or resume, if we’re already at the top of the stack)
