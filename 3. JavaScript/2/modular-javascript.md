# Modular JavaScript

In 2001, Douglas Crockford introduced the concept of [private members in JavaScript](http://javascript.crockford.com/private.html). By 2007, people were calling this the [module pattern](http://yuiblog.com/blog/2007/06/12/module-pattern/) and soon after it was in widespread use as a way of not polluting the global namespace.

[Native modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) are coming in ES6, but as of June 2016 no major browser supports the new syntax.

For the foreseeable future, you can implement JavaScript modules in one of the following ways:

1. In an [IIFE](http://benalman.com/news/2010/11/immediately-invoked-function-expression/)
2. Using a 3rd party library
3. Via dependency resolution using a build step
4. Using a transpiler.

------

## IIFE

IIFE stands for “immediately invoked function expression”. The term was coined by Ben Alman in 2010 to accurately describe the following design pattern:

    var myModule = (function () {
        var my_private_var = 42;
        var my_public_var = 'foo';

        function myPrivateMethod() {
            alert('you can’t call me!');
        }

        function myPublicMethod() {
            console.log(my_private_var);
        }

        return {
            my_public_var: my_public_var,
            myPublicMethod: myPublicMethod
        };
    }());

    myModule.my_private_var // undefined
    myModule.my_public_var // 'foo'

    myModule.myPrivateMethod() // TypeError
    myModule.myPublicMethod() // 42;

The advantage of the above is that the module is able to maintain its own state without other code accidentally (or intentionally!) futzing (that’s a technical term) with it.

------

## Third Party Libraries

[RequireJS](http://requirejs.org/) is by far the most popular library for creating and using modular JavaScript in the browser.

Example:

    // mymodule.js
    define(function () {
        return function () {
            alert('foo');
        };
    });

    // app.js
    requirejs(['./mymodule'], function (sayFoo) {
        sayFoo(); // alert('foo');
    });

RequireJS works well, but it has a clunky syntax and you have to be careful when adding or removing dependencies to update the list of arguments correctly.

------

## Dependency Resolution

If you have a build step in your project (e.g., using [Gulp](http://gulpjs.com/)), you can use RequireJS to help you package up your JavaScript dependencies in a way that’s more performant than running RequireJS in the browser.

------

## Transpilers

The [Babel transpiler](https://babeljs.io/) allows you to use ES6 features, including the native `import` syntax in your JavaScript. Using Gulp (or another task runner), you can use Babel to transpile your ES6 back to JavaScript that will run in the browser.
