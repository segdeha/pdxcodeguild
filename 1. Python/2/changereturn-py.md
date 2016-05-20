# changereturn.py

## Objective

Some supermarkets have automatic change dispensers. Let’s write code that figures out how to divvy up an amount of change into the _fewest_ quarters, dimes, nickels, and pennies.

1. Open Atom
1. Create a new file and save it as `changereturn.py`
1. Implement a simple program that satisfies the following requirements:
    * Ask for the amount of change to dispense _in cents._ Assume that number will be less than or 100.
    * Calculate the number of quarters necessary first.
    * Then calculate the number of dimes, nickels, and pennies. If you do it in that order, you will minimize the number of coins.

**Hint:** This is easiest done by updating a _running total_ of number of cents left to be put into coins. Also remember that the `//` operator divides and removes any remainder.

## Advanced

* Print out the total number of coins
* Expand this problem to work on cents >100 and include bills
* Store how many of each coin is in the cash register, then allow the change algorithm to deal with when you don’t have enough coins to optimally give change
