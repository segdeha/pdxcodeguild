# Operators and Expressions

Programming is giving instructions to the computer to transform some input data into different output data.

The most basic way is via an **operator.** Operators take in multiple input **arguments** and **return** a single output value. Operators are the basic verbs of programming.

    argument value -\
                     >-- operator --> return value
    argument value -/

You’ve seen operators in math class:

    3 + 6 = 9
    100 - 200 = -100

Anything that returns a value is called an **expression.** Both literals and operators with inputs are expressions.

In these notes, whenever you see `#>`, I’m showing you the return value of the preceding expression.

Python gives you all of the usual math operators that work on ints and floats:

    3 + 6  #> 9
    100 - 200  #> -100
    5 * 2  #> 10
    9.9 - 0.1  #> 9.8
    40 / 80  #> 0.5

It also gives you operators that work on strings:

    'Hi, ' + 'David'  #> 'Hi, David'

As a rule-of-thumb, operators only make sense on like types, so avoid:

    'Hi' + 6.0  #> throws TypeError
