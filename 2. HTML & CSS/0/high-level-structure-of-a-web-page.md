# High-Level Structure of a Web Page

The following is the minimum, correct code for a complete web page:

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>My Awesome Page</title>
        </head>
        <body>

            <!-- content goes here -->

        </body>
    </html>

Let’s break it down.

- `<!doctype html>` — Tells the browser to use version 5 of HTML (see here for [other doctypes](http://www.htmlhelp.com/tools/validator/doctype.html))
- `<html></html>` — Container for the entire page
- `<head></head>` — Meta information about the page
    - `<meta charset="utf-8">` — Tells the browser which character encoding to use (**always** use UTF-8; you may see one of these [legacy encodings](https://encoding.spec.whatwg.org/#encodings) on older web sites)
    - `<title></title>` — What shows up in the browser title bar
- `<body></body>` — Visible content of the page

------

1. [What Every Programmer Absolutely, Positively Needs To Know About Encodings And Character Sets To Work With Text](http://kunststube.net/encoding/)