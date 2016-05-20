# Basic Debugging

You _will_ make mistakes. That’s expected! The computer will tell you what is wrong _if you listen._

Use the following two ideas to help you solve problems. **I cannot stress strongly enough** how these techniques will help.

------

## Listen to Errors

**Exceptions** are errors. They are **thrown** from a specific line of code when something is wrong.

They are so great! They tell you the exact file, line, and what is wrong.

Look at the _bottom_ of the error message:

    Traceback (most recent call last):
        MORE FUNCTIONS...
        File "test.py", line 1, in <module>
    TypeError: cannot concatenate 'str' and 'int' objects

* `NameError` — No variable or function known by that name
* `ValueError` — A value you’re using doesn’t make sense in the context
* `TypeError` — You’re using the wrong type
* `SyntaxError` — Your Python is written incorrectly

------

## Double Check Mental Model

Data is invisible unless you print it.

* Double check each operation is returning what you expect.
* Double check inputs, not just outputs; garbage in, garbage out
* Do this on an operation-by-operation basis
* Avoid long strings of operations; assign to variables after each step to print

Can you spot the error?

    miles = 300.0
    mpg = 28.0
    dollars_per_gallon = 2.80
    people_on_trip = 4
    cost_per_person = miles / mpg / dollars_per_gallon / people_on_trip

If you print out intermediate values, it will be easier to see what you messed up.

    miles = 300.0
    mpg = 28.0
    dollars_per_gallon = 2.80
    people_on_trip = 4
    gallons = miles / mpg
    print(gallons)
    total_gas_cost = gallons / dollars_per_gallon
    print(total_gas_cost)
    cost_per_person = total_gas_cost / people_on_trip
    print(cost_per_person)

Remove these debug prints when you’re done.
