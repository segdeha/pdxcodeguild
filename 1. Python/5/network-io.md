# Network I/O

Reading and writing files on disk is great and all, but that only works if you already have the data you need locally. There is a ton of [interesting data available on the internet](https://www.publicapis.com/), so let’s learn how to use it!

The `urllib.request` module allows you to make network requests. It’s similar to [reading files from disk](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/4/file-io.md), with a couple of differences:

- The result is returned as binary data by default, so you have to convert it to text before you can, for example, convert it to JSON.
- You don’t have to `close` the handle.

Example:

    import urllib.request
    
    handle = urllib.request.urlopen('http://www.example.com/')
    contents = handle.read()
    text = contents.decode('utf-8')
    
    print(text)

------

Sources:

1. [urllib.request — Extensible library for opening URLs](https://docs.python.org/3.5/library/urllib.request.html)