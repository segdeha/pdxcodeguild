# Anatomy of a Web Page

Web pages consist of HTML, CSS, and JavaScript. They’re kind of like birthday cakes.

------

HTML is the cake. It’s covered with CSS frosting that makes it look pretty. Then you add some JavaScript to the top to give it a little sparkle.

![Birthday cake with candles](http://theartmad.com/wp-content/uploads/2015/08/Happy-Birthday-Cake-Pictures-With-Candle-2.jpg)

------

It’s totally possible to build a beautiful, tasty web page with only HTML and CSS.

![Simple chocolate cake](https://i.ytimg.com/vi/hKeKuuAll8Y/maxresdefault.jpg)

------

And it’s totally possible to go crazy with JavaScript and make a cake that’s a serious fire hazard (we call those [single-page apps](https://en.wikipedia.org/wiki/Single-page_application) [I kid. {Kind of.}]).

![Crazy cake](https://s-media-cache-ak0.pinimg.com/736x/35/1b/0a/351b0aa8774276354c8e6d24b6fc53c9.jpg)

------

We’ve seen the following basic structure of a web page before:

    <!doctype html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>My Awesome Page</title>
            <link href="styles.css">
            <script defer src="behaviors.js"></script>
        </head>
        <body>
            <h1>My Awesome Page</h1>
            <p>Stuff I want to say.</p>
        </body>
    </html>

- HTML is responsible for providing semantic structure to the content of the page.
- CSS provides presentation to the content
- JavaScript provides dynamic, interactive behaviors to the page

------

All three of HTML, CSS, and JavaScript are just text files written in different syntaxes. Web browsers know how to interpret all three and allow them to work together to provide a unified experience of what we call a web page.
