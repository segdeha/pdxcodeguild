# JavaScript Language Basics

Many of the concepts you learned in Python have corollaries in JavaScript. Let’s run through a few of them.

------

## Whitespace

Let’s get this out of the way. JavaScript is **way** more lenient about whitespace than Python! Indentation doesn’t mean anything in JavaScript.

You have to use spaces to separate certain keywords, but otherwise, you can literally have all of your JavaScript on one line if you want to.

Example:

    function myFunc( a, b ) {
        var c = a + b;
        return c > 10;
    }

The above is functionally equivalent to the following:

    function myFunc(a,b){var c=a+b;return c>10;}

_Of course, we code for readability over conciseness, but removing extra whitespace is a common build step (called “minification”) before deploying JavaScript and CSS to the web._

------

## Primitives

[Primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) are JavaScript types that are not objects and have no methods. Examples include strings, numbers, and booleans, but also include `undefined` and `null`. They are the values, the data.

Examples:

    2 // number
    2.2222222 // number
    '2' // string
    true // boolean
    undefined
    null

------

## Types

JavaScript is what is called a “loosely typed” language. Unlike Python, manually casting values to specific types is rarely needed. JavaScript, supports the following types:

- `string` — Text (JavaScript is _mostly_ Unicode clean, except regular expressions)
- `number` — JavaScript makes no distinction between ints and floats
- `boolean` — Either `true` or `false`
- `Undefined` — A variable that has not been given a value
- `Null` — Similar to `Undefined`, but usually used to show that a variable is intentionally not defined
- `Object` — The only type that is not a “primitive” and the basis for everything in the language that is not a primitive

### Mini-excercise: Understanding type coercion

JavaScript will attempt to coerce your data to the correct type depending on the operation you are trying to execute. In the browser console or in a Node shell, try the following:

    2 + 2 // 4
    'two' + 'two' // 'twotwo'
    2 + '2' // '22'
    2 * '2' // 4

------

## Objects

In JavaScript, anything that is not a primitive is an object. That includes functions, arrays, regular expressions, etc. Much like Python classes, objects are containers for properties (values) and methods (functions).

JavaScript’s concept of objects is more flexible than most languages. For example, you can create a function in JavaScript and then attach arbitrary properties to it like any other object.



------

## Variables

As we know from Python, variables are containers for values. The syntax in JavaScript is as follows:

    var my_var = 'hello world';

_Note: You must use the `var` keyword when you create variables._

------

## Loops

Python has some nicer ways of creating loops, but you can do most of the same things in JavaScript.

Example:

    for (var i = 0; i < 10; i += 1) {
        console.log('hello world');
    }

    var i = 0;
    while (i < 10) {
        console.log('hello world');
        i += 1;
    }

    var i = 0;
    do {
        console.log('hello world');
        i += 1;
    } while (i < 10);

------

## Conditionals

The syntax for branching is similar in JavaScript to Python. There’s also an additional construct called a `switch` statement.

Example:

    if (my_var === 'a') {
        console.log('we love a!');
    }
    else if (my_var === 'b') {
        console.log('we love b!');
    }
    else {
        console.log('we love c!');
    }

    switch (my_var) {
        case 'a':
            console.log('we love a!');
        break;
        case 'b':
            console.log('we love b!');
        break;
        default:
            console.log('we love c!');
        break;
    }

------

## Arrays

Whereas Python has lists and dictionaries, JavaScript has arrays and associative arrays (or, simply, objects). The syntax is similar, except for which type of braces you use for each.

Example:

    var my_array = [ 'a', 'b', 'c' ];
    var my_object = {
        a: 1,
        b: 2,
        c: 3
    };

    my_array[ 1 ]; // 'b'
    my_object[ 'c' ]; // 3

_Associative arrays (equivalent to Python dictionaries) are just objects in JavaScript. See the section below for more about objects._

------

## Comments

You can write comments in JavaScript in two ways, similar to Python.

Example:

    // this is a single-line comment
    /* this is a
       multi-line comment */

------

Sources:

1. [Standard built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)
1. [JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
1. [Unicode and JavaScript](http://www.2ality.com/2013/09/javascript-unicode.html)


