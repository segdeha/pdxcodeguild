# JavaScript

JavaScript is the _lingua franca_ of the web. Where HTML adds structure, and CSS adds presentation, JavaScript adds behaviors to web pages.

JavaScript runs on the server as well. It is possible to build complete web applications in JavaScript. You can write the backend in [Node.js](https://nodejs.org/), [Express](http://expressjs.com/), and [MongoDB](https://www.mongodb.com/) ([among](http://koajs.com/) [other](http://hapijs.com/) [options](http://couchdb.apache.org/)) and the frontend in [React](https://facebook.github.io/react/), [Redux](https://github.com/reactjs/redux), and [jQuery](https://jquery.com/) ([among](http://riotjs.com/) [other](https://angularjs.org/) [options](http://emberjs.com/)) for even the most complex of web apps.

JavaScript is even used for build tools, as we saw when working with [Sass]() and [Gulp](http://gulpjs.com/). You can literally use JavaScript to drive every layer of your web application stack.

_Note: The spec is actually called [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript), but we’re going to use the colloquial name, JavaScript._

------

## A Little History

[JavaScript](https://en.wikipedia.org/wiki/JavaScript), the language, was written by [Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich) in just 10 days.

The marketing folks at [Netscape](https://en.wikipedia.org/wiki/Netscape) wanted to capitalize on the popularity of [Java](https://en.wikipedia.org/wiki/Java_(programming_language)), so they had him make it look kind of like Java and they called it JavaScript, dooming entire generations of recruiters to alienate potential frontend developer clients by asking them “Do you know HTML, CSS, and Java?”

------

## Mini-Exercise: Hello World

JavaScript needs an environment in which to run. Luckily, we already have two on our systems, so let’s do our `Hello World` ~~two~~ three ways!

### In the browser

1. In your web browser, right click and choose “Inspect” or “Inspect Element” to bring up the web inspector
1. Switch over to the “Console” tab in the web inspector
1. Enter the following, then hit [enter]: `console.log('Hello World');`

![Result of running console.log in the browser](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/3.%20JavaScript/assets/hello-world-browser.png?token=AAAQ0luoNdgEkKOnlXMZXT5ejSp9LLXbks5XZvQcwA%3D%3D)

### In Node.js

1. In the Terminal, type the following then hit [enter]: `node`
1. Now type the following then hit [enter]: `console.log('Hello World');`

![Result of running console.log in Node](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/3.%20JavaScript/assets/hello-world-node.png?token=AAAQ0q2uJmLn5KFtbnDokLfENTOTr8rQks5XZvQfwA%3D%3D)

_Same as in the Python shell, you can type [ctrl-d] to quit Node._

### In Node.js as a file

Just like in Python, you can tell Node to execute a file of JavaScript at the command line.

1. Create a new file called `hello-world.js`
1. Add the following line to the file: `console.log('Hello World');`
1. In the Terminal, `cd` into the directory where `hello-world.js` is and run the following: `node hello-world.js`

The program should print out `Hello World` and exit.
