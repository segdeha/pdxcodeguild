# Thinking Like a Programmer: Don’t Repeat Yourself

In most cases, you should strive to make your code DRY. DRY code has a single source of truth for all important knowledge (e.g., data, business rules, etc.).

> DRY says that every piece of system knowledge should have one authoritative, unambiguous representation.¹

Contrast this with WET code. WET in this context can stand for any or all of the following²:

- “Write Everything Twice”
- “We Enjoy Typing”
- “Waste Everyone’s Time”

Clearly, we’d prefer our code to be DRY!

------

Example:

    from datetime import datetime
    
    dt1 = datetime.fromtimestamp(1161119047)
    dt2 = datetime.fromtimestamp(1382457301)
    dt3 = datetime.fromtimestamp(1058238077)
    
    print('{dt.month}/{dt.day}/{dt.year}'.format(dt=dt1))
    print('{dt.month}/{dt.day}/{dt.year}'.format(dt=dt2))
    print('{dt.month}/{dt.day}/{dt.year}'.format(dt=dt3))

This is pretty WET. Let’s make it DRY!

Example:

    from datetime import datetime
    
    def format_date(timestsamp):
        dt = datetime.fromtimestamp(timestsamp)
        return '{dt.month}/{dt.day}/{dt.year}'.format(dt=dt)

    print(format_date(1161119047))
    print(format_date(1382457301))
    print(format_date(1058238077))

Better, right? It’s the same number of lines of code, but now the knowledge for how to format our date string lives in one place. As a bonus, our new `format_date` function is a pure function, so it’s testable as well!

Ideally, throughout whatever project the above is part, this function should be used to format all date strings. If you need different formats in different places, you could extend this function to take an additional, optional parameter to specify the various formats.

------

Sources:

1. [Orthogonality and the DRY Principle](http://www.artima.com/intv/dry.html)
1. Wikipedia entry on [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)