# Python 2 versus Python 3

Many of the examples you’ll find around the web are written in Python 2 and won’t run unmodified on the Python 3 interpreter we’re using.

You can read all about [the differences between Python 2 and 3](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html), but the main ones you’re likely to run into are the following:

------

## `print` is now a function

Python 2:

    print 'hello'

Python 3:

    print('hello')

------

## Integer division changed

Python 2:

    3 / 2  #> 1
    3 / 2.0  #> 1.5

Python 3:

    3 / 2  #> 1.5
    3 / 2.0  #> 1.5

------

## Python 3 strings are now UTF-8

Python 2:

    print('This string is not \u03BCnico\u0394é!')  #> This string is not \u03BCnico\u0394é!

Python 3:

    print('This string is \u03BCnico\u0394é!')  #> This string is μnicoΔé!

------

## No more `xrange`, use `range`

Python 2:

    for i in xrange(10):
        print(i)

Python 3:

    for i in range(10):
        print(i)

------

## No more `raw_input`, use `input`

Python 2:

    raw_input('Enter your favorite insect: ')

Python 3:

    input('Enter your favorite insect: ')
