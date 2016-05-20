# Ternary Operators

Python doesn't have C-style ternary operators.

    [condition] ? [true expression] : [false expression]

In JavaScript, for example, you can do the following:

    var desc = age < 12 ? 'young' : 'old';

The pythonic way of accomplishing the above is one of the following:

    [true expression] if [condition] else [false expression]

...or using a tuple...

    ([false expression], [true expression])[[condition]]

Examples:

    desc = 'young' if age < 12 else 'old'
    desc = ('old', 'young')[age < 12]
