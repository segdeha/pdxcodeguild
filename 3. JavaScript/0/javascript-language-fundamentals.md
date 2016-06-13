# JavaScript Language Fundamentals

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

## Variables

As we know from Python, variables are containers for values. The syntax in JavaScript is as follows:

    var my_var = 'hello world';

_Note: You must use the `var` keyword when you create variables._

------

## Primitives

[Primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) are JavaScript types that are not objects and have no methods. Examples include strings, numbers, and booleans, but also include `undefined` and `null`. In your programs, they are the values, the data.

Examples:

    2 // number
    2.2222222 // number
    '2' // string
    true // boolean
    undefined
    null

### Mini-exercise: typeof

In the browser console, type `typeof` followed by different primitive values and see what JavaScript tells you they are.

Example:

    typeof 'foo' // 'string'

------

## Operators

JavaScript shares many, but not all, of the operators available in Python. We’ve already seen one of them above, the assignment operator (`=`). The following are a few examples of the operators available in JavaScript (see [Mozilla Developer Network’s documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators) for a complete list):

    var a = 1; // 1
    a += 2; // 3

    'a' + 'b' // 'ab'

    1 == 1 // true
    1 == 2 // false
    1 != 2 // true

    1 === 1 // true
    1 === 2 // false
    1 !== 2 // true

    1 > 2 // false
    1 < 2 // true
    1 >= 2 // false
    1 <= 2 // true

    1 + 2 // 3
    1 - 2 // -1
    1 * 2 // 2
    1 / 2 // 0.5
    1 % 2 // 1

    true && false // false
    true || false // true
    !(true && false) // true
    !(true || false) // false

    typeof 'foo' // 'string'
    typeof 42 // 'number'

    1 in ['foo', 'bar', 'baz'] // true
    3 in ['foo', 'bar', 'baz'] // false

    'foo' in { 'foo': 'bar' } // true
    'baz' in { 'foo': 'bar' } // false

_Note: JavaScript supports comparisons using both the `==` and `===` operators. They are not the same! `==` [coerces](https://github.com/getify/You-Dont-Know-JS/blob/master/types%20%26%20grammar/ch4.md) the values in an attempt to compare apples to apples whereas `===` compares first the type, then the value._

------

## Types

JavaScript is what is called a “loosely typed” language. Unlike Python, manually casting values to specific types is rarely needed. JavaScript, supports the following types:

- `string` — Text (JavaScript is _mostly_ Unicode clean, the major exception being regular expressions)
- `number` — JavaScript makes no distinction between ints and floats
- `boolean` — Either `true` or `false`
- `undefined` — A variable that has not been given a value
- `null` — Similar to `undefined`, but usually used to show that a variable is _intentionally_ not defined
- `object` — The only type that is not a “primitive” and the basis for everything in the language that is not a primitive

### Mini-excercise: Understanding type coercion

JavaScript will attempt to coerce your data to the correct type depending on the operation you are trying to execute. In the browser console, try the following:

    2 + 2 // 4
    'two' + 'two' // 'twotwo'
    2 + '2' // '22'
    2 * '2' // 4
    2 + undefined // NaN
    2 + null // 2

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

## Objects

In JavaScript, anything that is not a primitive is an object. That includes functions, arrays, regular expressions, etc. Much like Python classes, objects are containers for properties (values) and methods (functions).

JavaScript’s concept of objects is more flexible than most languages. For example, you can create a function in JavaScript and then attach arbitrary properties to it like any other object.

You can create objects in several ways (it’s also accurate to say that you almost can’t help creating objects in JavaScript!). As a data structure, the simplest way to create an object is using the “object literal” syntax.

Example:

    var my_obj = {
        foo: 'bar',
        baz: 'qux'
    };

You can then access properties of the object using either dot or square bracket notation.

Example:

    my_obj.foo // 'bar'
    my_obj['baz'] // 'qux'

More complex objects contain both properties and methods. For example, take JavaScript’s built-in `Math` object.

Example:

    Math.PI // 3.141592653589793
    Math.max(123, 45) // 123

### Mini-exercise: Inspect the Math object

In the browser console, inspect the `Math` object by typing in `Math` and hitting [enter]. Try out some of the methods to better understand what they do.

------

## Functions

JavaScript functions behave similarly to functions in Python. They take arguments and return values. Unlike in Python, where you can set default values in the method signature, all arguments in JavaScript are positional arguments.

Example:

    function myFunc(a, b) {
        console.log(a, b);
    }

    myFunc(1, 2); // 1 2

Unlike Python, JavaScript will not complain if you call a function with the wrong number of positional arguments. What will happen is those arguments will take the value `undefined`.

If you want your arguments to have default values, you will need to do that work inside the function.

Example:

    function myFunc(a, b) {
        a = a || 1;
        b = b || 2;
        console.log(a, b);
    }

    myFunc(); // 1 2

When executed, all JavaScript functions create an `arguments` object that functions similarly to an array.

Example:

    function myFunc() {
        console.log(arguments[0], arguments[1]);
    }

    myFunc(1, 2); // 1 2

By default, JavaScript functions return the value `undefined`, but you can (and in most cases, will want to) specify a return value.

Example:

    function addNumbers(num1, num2) {
        return num1 + num2;
    }

    var total = addNumbers(10, 5);
    console.log(total) // 15

Functions can even return other functions! This is a pattern worth getting used to because it is used **a lot** in JavaScript.

Example:

    function say(greeting) {
        return function (subject) {
            console.log(greeting + subject);
        };
    }

    var sayHello = say('Hello');

    sayHello('World'); // 'HelloWorld'

------

## Loops

Python has some nice convenience functions for creating loops (e.g., `range`), but you can do most of the same things in JavaScript.

Example:

    for (var i = 0; i < 10; i += 1) {
        console.log('hello world');
    }

    var my_obj = {
        foo: 'bar',
        baz: 'qux'
    };
    for (var p in my_obj) {
        console.log(p, my_obj[p]);
    }

_Note: Just like Python dictionaries, JavaScript object properties are not guartanteed to be returned in any particular order!_

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

Arrays also have the following specialized method for looping over their elements:

    ['foo', 'bar', 'baz'].forEach(function (item) {
        console.log(item);
    });

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

## Comments

You can write comments in JavaScript in two ways, similar to Python.

Example:

    // this is a single-line comment
    /* this is a
       multi-line comment */

------

Sources:

1. [Standard built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)
1. [Expressions and operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators)
1. [JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
1. [Unicode and JavaScript](http://www.2ality.com/2013/09/javascript-unicode.html)
1. [typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

