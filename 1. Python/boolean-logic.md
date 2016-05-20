# Boolean Logic

[Booleans](https://en.wikipedia.org/wiki/Boolean_data_type) are a data type that represents yes/no, true/false, 1/0.

In Python (it’s different in other languages), these are represented by the words `True` and `False`, exactly as written here. No quotes and capitalized.

Just like `int`, `str`, and `float`, there is a `bool` type you can use to cast a value to a Boolean or determine whether something is of the Boolean type.

The results can be surprising.

    >>> bool(1)
    True
    >>> bool(0)
    False
    >>> bool(-1)
    True
    >>> bool('hello')
    True
    >>> bool('')
    False
    >>> isinstance(1, bool)
    False
    >>> isinstance(True, bool)
    True
    >>> isinstance(1 < 2, bool)
    True

Booleans form the basis of all branching within our programs. If your program is not behaving as you expect it to, double-check that the values you’re using in comparisons are evaluating as expected.

## `and` & `or`

It’s important to understand how your program is going to branch when faced with a complex Boolean. The following are examples of how Python evaluates various ‘this’ and/or ‘that’ combinations.

You don’t have to memorize these, but remember that your `if` statements are governed by this Boolean logic. Come back to this list as reference as needed.

    >>> 'a' and 'b'
    'b'
    >>> 'a' or 'b'
    'a'
    >>> True and False
    False
    >>> True or False
    True
    >>> True and True
    True
    >>> True or True
    True
    >>> False and False
    False
    >>> False or False
    False
    >>> False and True
    False
    >>> False or True
    True
    >>> not True or False
    False
    >>> not False or True
    True
    >>> True or not False
    True
    >>> False or not True
    False
    >>> not True and not False
    False
    >>> not True or not False
    True

## Formal Logic

There is a whole branch of philosophy dedicated to formal logic. It tells us (among other things) the following:

    NOT(A AND B) == NOT(A) OR NOT(B)

and

    NOT(A OR B) == NOT(A) AND NOT(B)

Formal logic is beyond the scope of this course, but the rabbit hole is there if you want to go down it!
