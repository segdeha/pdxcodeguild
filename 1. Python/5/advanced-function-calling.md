# Advanced Function Calling

## Passing by Position

Thus far, we’ve been passing arguments to functions **by position.**
The values at the call site are bound to the variables in the function signature _in order._

    def subtract(a, b):
      return a - b
    
    subtract(5, 8)  #> -3
    # a = 5; b = 8

## Optional Arguments

Most positional arguments are like the above, **required arguments.** But it’s also possible to have functions that take **optional arguments.**

If they are specified when the function is called, then the caller’s value is used. Otherwise, the default value from the function definition is used.

    def subtract(a, b=1):
      return a - b
    
    subtract(5)  #> 4
    # a = 5; b = 1
    
    subtract(5, 8)  #> -3
    # a = 5; b = 8

## Passing by Keyword

Optional arguments may also be passed **by keyword** _in any order,_ as long as they come after all positional arguments.

    def subtract(a, b=1, c=0):
      return a - b - c
    
    subtract(5, b=8)  #> -3
    # a = 5; b = 8; c = 1
    
    subtract(5, c=9)  #> -5
    # a = 5; b = 1; c = 9
    
    subtract(5, c=9, b=8)  #> -12
    # a = 5; b = 8; c = 9

## \*args & \*\*kwargs

When reading more advanced Python code, you might see functions written like the following:

    def print_movie_ratings(username, *args, **kwargs):
        """Update the user’s ratings for movies.
        Update movies from *args that are keys in **kwargs.
        """
        for arg in args:  # Loop through the tuple `args`
            if arg in kwargs:  # Loop through keys of the `kwargs` dictionary
                print(arg, kwargs[arg])

    print_movie_ratings('segdeha', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)
    
    """ Output is:
    Sharknado 3
    Frozen 2
    """

This syntax is used to create functions that can take a varying number of arguments.

_Note: The special thing about these variable names isn’t `args` and `kwargs`. It’s the `*` and `**`. You can name these arguments anything that’s a legal variable name, but by convention they’re named `*args` and `**kwargs`._

Within the function above, `*args` is defined as a tuple of the positional arguments passed to the function that don’t have explicit names in our function signature.

Within our function, `**kwargs` is defined as a dictionary of any keyword arguments passed to the function that don’t match keywords in the function signature.

I don’t expect you to use `*args` and `**kwargs` in class, but I wanted to expose you to them so you could understand code you’ll see in the wild.

------

Sources:

1. [How to use *args and **kwargs in Python](http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/)
