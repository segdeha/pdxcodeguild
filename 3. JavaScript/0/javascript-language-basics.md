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

------

## Comments

You can write comments in JavaScript in two ways, similar to Python.

Example:

    // this is a single-line comment
    /* this is a
       multi-line comment */

------

## Types

JavaScript is what is called a “loosely typed” language. Unlike Python, manually casting values to various types is rarely needed. JavaScript, supports the following types:

- `string` — Text
- `number` — JavaScript makes no distinction between ints and floats
- `boolean` — Either `true` or `false`
- `Undefined` — A variable that has not been given a value
- `Null` — Similar to `Undefined`, but usually used to show that a variable is intentionally not defined
- `Object` — The only type that is not a “primitive” and the basis for everything in the language that is not a primitive

------

## Objects

Objects deserve their own section because they are so ubiquitous in JavaScript.

------

Sources:

1. [JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
