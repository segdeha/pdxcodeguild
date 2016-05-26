# Advanced String Formatting

Until now, we’ve foramtted strings using the `format` method in the following way:

    # Pass values as a named arguments
    'My {adj1} {adj2} string'.format(
        adj1='super',
        adj2='awesome'
    )
    
    # Returns 'My super awesome string'

This works and is clear, which is why I taught it first. But `format` is actually more flexible than this.

------

Firstly, instead of passing in each keyword argument one-at-a-time, we can actually pass in a dictionary and spread the values. (Remember `**kwargs`? It’s not just for function definitions!)

Example:

    # Pass values as a dictionary
    adjectives = {
        adj1: 'super',
        adj2: 'awesome'
    }
    'My {adj1} {adj2} string'.format(**adjectives)
    
    # Returns 'My super awesome string'

------

In addition to named arguments, we can pass values as positional arguments.

Example:

    # Pass values as positional arguments
    'My {} {} string'.format('super', 'awesome')
    
    # Returns 'My super awesome string'

------

We can even reference positional arguments by the order they were passed in (0 indexed, just like a tuple).

Example:

    # Pass values as positional arguments
    'My {0} {1} string'.format('super', 'awesome')
    
    # Returns 'My super awesome string'

The cool thing about this is we can pass things in in one order and output them in another order.

Example:

    # Pass values as positional arguments
    'My {1} {0} string'.format('awesome', 'super')
    
    # Returns 'My super awesome string'

------

We can also pass complex objects and access their attributes within the template tokens.

Example:

    # Pass an object with attributes
    from datetime import datetime

    dt = datetime.fromtimestamp(1464061454)
    '{dt:%B} {dt.day}, {dt.year}'.format(dt=dt)
    
    # Returns 'May 23, 2016'

In the above example, we’re passing in `dt` (which is a `datetime` object) making it available to all of the replacement instances. `.day` and `.year` are attributes of the `dt` object.

Also, notice `dt:%B`. The `%B` part of that token is a formatting string that gets run against the `dt` object and returns, in this case, the name of the month associated with the date.

We’ll cover dates in another lesson. The point here is that you can access attributes of objects and even manipulate the strings before the output string is assembled.
