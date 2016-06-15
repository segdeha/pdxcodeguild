# Exercise: Return of Change Return!

_Note: This is the same exercise we did in Python only now we’re implementing it in JavaScript!_

## Objective

Some supermarkets have automatic change dispensers. Let’s write code that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.

1. Fork [this pen](http://codepen.io/segdeha/pen/LZNvMV) & name it “Change Return”
1. Implement a simple program that satisfies the following requirements:
    * Ask for the amount of change to dispense _in cents._ Assume that number will be less than or 100.
    * Calculate the number of quarters necessary first.
    * Then calculate the number of dimes, nickels, and pennies. If you do it in that order, you will minimize the number of coins.

**Hint:** This is easiest done by updating a _running total_ of number of cents left to be put into coins.

_Note: The `//` operator in JavaScript does not do what it does in Python, so you’ll need to find another way, e.g., using the `Math.floor` method._

------

## Extra Credit

* Instead of assuming your “cash register” has an unlimited number of coins of each type, randomly generate how many of each type of coin you have to work with before computing the change to give and adjust what coins you return based on what’s available; experiment with how many to generate, but start with 0 to 9 of each type

------

Sources:

1. [Math](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math) on Mozilla Developer Network
