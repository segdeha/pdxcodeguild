# I/O with `with`

Up to this point, we’ve worked with files like the following:

    f = open('filename.ext', 'r')  # > get handle to file
    contents = f.read()  # > read contents of the file
    f.close()  # > close file handle

I had us do it this way to expose you to what needs to happen when you work with files, but a more idiomatic (and concise!) way to do the same thing is as follows:

    with open('filename.txt', 'r') as f:
        contents = f.read()

I’ll skip the technical details (or, you can read about them [here](http://effbot.org/zone/python-with-statement.htm)), but suffice it to say this does the same thing, including closing the file handle!
