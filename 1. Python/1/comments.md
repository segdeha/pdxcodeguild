# Comments

If you want to write free-form information in your Python source, you can use **comments.**

Comments are any text after a `#`.

    # Anything can go here!
    three = 2 + 1  # You can put it after regular Python, too!

Use comments to:

1. Remind yourself how a section of code works
1. Disable one version of code you’re trying out to compare to another version
1. As a to-do list for things you need to fill in later

------

## Multi-line comments

Sometimes you need to write comments that span multiple lines. [PEP 8 recommends](http://legacy.python.org/dev/peps/pep-0008/#block-comments) using multiple, single-line comments (`#` style) unless the comment is what’s known as a documentation string or ‘docstring’.

Docstrings are (usually) multi-line comments, delimited by `'''`, that appear as the first content within a class, function, or module.

    '''
    This is a comment.
    It spans multiple lines.
    '''

You can read about how docstrings should be formatted in [PEP 257](https://www.python.org/dev/peps/pep-0257/).
