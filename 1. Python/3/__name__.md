# __name__

When Python executes a file, it sets a variable called `__name__` in the global scope of the script.

If the file is being executed directly (e.g., `>>> python my_file.py`), `__name__` will be set to the string `'__main__'`. If the file has been imported as a module from another script, `__name__` will be set to the module name.

A common use of this variable is to do something different based on whether the file has been imported or run directly. In other words, you can design your program either to be run or imported and have it behave differently in each case.

Example¹:

    if __name__ == '__main__':
    	print 'This program is being run directly'
    else:
    	print 'This program was imported from another module'

------

Sources:

1. [A module's __name__](http://ibiblio.org/g2swap/byteofpython/read/module-name.html)
