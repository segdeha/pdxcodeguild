# Date String Formatting

In the bad old days of Python (before version 3), formatting a date as a human-readable string required you to string together arcane formatting strings using the tokens found [here](https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior). Someone even created [a site dedicated just to these tokens](http://strftime.org/).

Say you wanted to represent the date and time I wrote this lesson as `'May 23, 2016, 20:44:14'`. The following is how you used to have to do it:

    from datetime import datetime

    dt = datetime.fromtimestamp(1464061454)
    dt.strftime('%B %d, %Y, %H:%M:%S')

Pretty gross.

In Python 3, we can do something a little more elegant.

    from datetime import datetime

    dt = datetime.fromtimestamp(1464061454)
    '{dt:%B} {dt.day}, {dt.year}, {dt.hour}:{dt.minute}:{dt.second}'.format(dt=dt)

Much better! But did you notice `dt:%B`? That’s what’s called a [leaky abstraction](https://en.wikipedia.org/wiki/Leaky_abstraction). That `%B` is an old-style formatting token that leaked through because the new way of formatting date strings doesn’t implement quite everything. Sorry, you might end up having to learn those suckers after all!

------

## Quick Exercise

Take a few minutes in the interactive shell to create some date objects and format them in different ways.

_Hint: Use the built-in `dir` method to discover what methods and attributes are available to you on a `datetime` object._

------

Sources:

1. Stack Overflow answer to [Python strftime - date without leading 0?](http://stackoverflow.com/a/16097385/11577)
1. Python 2.7 docs for [datetime — Basic date and time types](https://docs.python.org/2/library/datetime.html)
