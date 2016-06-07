# Sass

[Sass](http://sass-lang.com/) stands for “Syntactically Awesome Style Sheets”. It provides a bunch of helpful, additional functionality to standard CSS.

_Note: There are two flavors of Sass syntax to choose from. We’re going to use what’s called **SCSS** because it’s more like regular CSS than the original, legacy Sass syntax._

------

## Selector Nesting

Manually maintaining complex selectors can be a pain. Sass makes it easier to understand what’s going on in your style sheet by allowing you to nest selectors.

Example:

    figure {
        float: right;
        img {
            border: solid 1px black;
        }
    }

Sass compiles the above to the following:

    figure {
        float: right;
    }
    figure img {
        border: solid 1px black;
    }

------

## Variables

Variables are coming in future versions of CSS, but you can take advantage of this feature now to simplify your CSS using Sass.

Example:

    $link-color: #0cf;

    a {
        color: $link-color;
    }

Sass compiles the above to the following:

    a {
        color: #0cf;
    }

------

## Mixins

Mixins are JavaScript-like functions you can use to programmatically create CSS at compile-time.

Example:

    @mixin range-pct {
        @for $i from 0 through 100 {
            input[type=range].pct#{$i}:after { width: percentage($i/100) }
        }
    }

    @include range-pct;

Sass compiles the above to the following:

    input[type=range].pct0:after { width: 0% }
    input[type=range].pct1:after { width: 1% }
    input[type=range].pct2:after { width: 2% }
    ...
    input[type=range].pct100:after { width: 100% }

_Notice in the above an example of using standard math operators in your Sass functions!_

------

## Imports

Just like you split up your Python or JavaScript files into modules based on responsibility, you can do the same with your CSS using Sass imports. This is super helpful for keeping a big codebase modular, allowing multiple developers to contribute without stepping on each other’s toes.

Example:

    /* _typography.scss */
    body {
        font: 16px/1.33 Helvetica, Sans-Serif;
    }

Given the Sass file above (called a “partial” because of the leading underscore), you can import it into another file as follows:

    /* styles.scss */
    @import '_typography.scss';

    h1 {
        color: navy;
    }

Sass will compile the above to the following:

    body {
        font: 16px/1.33 Helvetica, Sans-Serif;
    }

    h1 {
        color: navy;
    }

## Inheritance

Just like we do in Python and JavaScript, we should strive to keep our CSS [DRY](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/5/dont-repeat-yourself.md). Sass helps us do this by allowing us to share a set of CSS properties across selectors.

Example (from [the official Sass guide](http://sass-lang.com/guide)):

    .message {
        border: 1px solid #ccc;
        padding: 10px;
        color: #333;
    }

    .success {
        @extend .message;
        border-color: green;
    }

    .error {
        @extend .message;
        border-color: red;
    }

    .warning {
        @extend .message;
        border-color: yellow;
    }

Sass compiles the above to the following:

    .message, .success, .error, .warning {
        border: 1px solid #cccccc;
        padding: 10px;
        color: #333;
    }

    .success {
        border-color: green;
    }

    .error {
        border-color: red;
    }

    .warning {
        border-color: yellow;
    }

------

That’s most of what we’ll be using in class, but do read over [the official Sass guide](http://sass-lang.com/guide) and [the full documentation](http://sass-lang.com/documentation/file.SASS_REFERENCE.html) to get more familiar with this powerful tool.
