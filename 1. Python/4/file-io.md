# File I/O

A common requirement of many programs is to read from and write to the computer’s filesystem. It should come as no surprise that Python has robust, built-in methods for accomplishing these tasks!

The `io` module has methods for reading and writing text, binary, and raw data.

_It’s rare that you’ll need to work with binary or raw data, so we won’t be covering those topics. Read up on them [here](https://docs.python.org/3/library/io.html#buffered-streams) and [here](https://docs.python.org/3/library/io.html#io.RawIOBase), if you’re curious._

## Working With Text Files

The `open` function allows you to open a file on the file system. Once you have opened the file, you can do things like read from and write to it.

You call `open` in one of several modes. The common ones we will be using are listed below.

- `'r'` — open for reading (default, though I like to specify it for clarity)
- `'w'` — open for writing, truncating the file first
- `'x'` — open for creation, failing if the file already exists
- `'a'` — open for writing, appending to the end of the file if it exists

Read the [full documentation](https://docs.python.org/3/library/functions.html#open) for more options.

Example:

    # Assume 'my_file.txt' exists and contains 'This is such a cool file.'
    
    f = open('my_file.txt', 'r')
    contents = f.read()
    past_tense = contents.replace(' is ', ' was ')
    f.close()
    
    f = open('my_file.txt', 'w')
    f.write(past_tense)
    f.close()
    
    # 'my_file.txt' now contains 'This was such a cool file.'

Note: It might seem clunky to have to open the file twice, once to read and once to write, but to keep things simple, safe, and predictable, Python only allows you to do one type of operation on a file at a time.
