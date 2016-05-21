# Exception Handling

Remembering back to the lesson on [basic debugging](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/2/basic-debugging.md), we learned that ‘exepctions’ are ‘thrown’ by Python when it can’t interpret what your program is trying to do.

Example:

    Traceback (most recent call last):
        MORE FUNCTIONS...
        File "test.py", line 1, in <module>
    TypeError: cannot concatenate 'str' and 'int' objects

Python supports the following 4 types of errors (by default, you can create your own!):

* `NameError` — No variable or function known by that name
* `ValueError` — A value you’re using doesn’t make sense in the context
* `TypeError` — You’re using the wrong type
* `SyntaxError` — Your Python is written incorrectly
* `KeyError` — The key you’re trying to access is not present in the dictionary

An elegant way to make your program more robust is to ‘catch’ thrown errors using what’s called a `try`/`except` block.

Example:

    try:
        this_wont_work = 1 + 'hello'
    except TypeError:
        print('That didn’t work!')

A common exception you might want to handle is when you try to access a key that doesn’t exist in a dictionary.

Example:

    my_dict = {'foo':'bar'}
    try:
        my_value = my_dict['baz']
    except KeyError:
        print('Try again!')

You can read more about exeption handling in the official [Python documentation](https://docs.python.org/3/tutorial/errors.html).
