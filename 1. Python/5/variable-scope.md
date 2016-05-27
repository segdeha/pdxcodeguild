# Variable Scope

Variables are delared within what is called a scope. That means they are available to different parts of your program depending on how and where they’re declared.

Why is this important?

## Name Resolution

You may see references to “LGB” in the context of Python. This refers to name lookups being done in either the local, global, or built-in scopes.

_Note: All names are unique within the scope where they are created. In other words, at any one time, there is only one variable or function with a particular name._

When Python encounters the name for something in code, it checks first for a match in the local scope. If it doesn’t find one, then it checks for a match in the global scope. If it doesn’t find one there, it checks the list of built-in functions.

**Python checks the scopes in LGB order and stops when it finds a match.**

Even though Python checks in LGB order, let’s talk about global variables first because they most closely match a lay person’s expectations about how variables should behave.

## Global Variables

A variable is considered a global when it is created at the file or module level. You can use the `global` keyword to gain the ability to _change_ global variables within functions in the same file or module. You can _read_ global variables without using the `global` keyword.

Example:

    global_var = 0
    
    def inc_global_var():
        global global_var
        global_var += 1
        print(global_var)
    
    inc_global_var()  #> 1
    inc_global_var()  #> 2
    
    global_var  #> 2

By creating a global variable, when we change its value, we’re changing the value of the variable everywhere it’s used.

Example:

    def print_global_var():
        global global_var
        print(global_var)
    
    print_global_var()  #> 2

## Local Variables

Contrast that with a local variable, i.e. one that is created within a function. Variables created within a function are created anew every time the function runs. And they are not available outside the function.

Example:

    def inc_local_var():
        local_var = 0
        local_var += 1
        print(local_var)
    
    inc_local_var()  #> 1
    inc_local_var()  #> 1
    
    local_var  #> Throws `NameError: name 'local_var' is not defined`

Additionally, if we try to access a local variable from another function, it won’t work, either.

Example:

    def print_local_var():
        print(local_var)
    
    print_local_var()  #> Throws NameError: name 'local_var' is not defined

## Built-ins

We covered how locals and globals work above. As the name implies, built-ins refers to [functions that are built-in to Python](http://www.programiz.com/python-programming/built-in-function).

These are similar to globals in that they are available everywhere. The difference is you don’t have to delcare them as globals within your functions to use them.

Example:

    len(['a', 'b', 'c'])  #> 3
    
    def print_len():
        print(len(['x', 'y', 'z']))  #> 3
