# Regular Expressions

Regular expressions (regex) are patterns used to match character combinations in strings.

In JavaScript, you can either call methods on a regular expression object or you can use regex in methods called on strings.

Example:

    var re = /a/;
    re.test('a'); // true

    var a = 'a';
    a.match(/a/); // ["a"]

------

## Creating Patterns

There are two ways to create regex patterns. We’re going to cover creating what’s called a “regular expression literal”, but if you’re interested in learning the other way, you can read about it in [MDN’s documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions).

Regex patterns consist of two slashes with characters between them, followed by one or more optional modifiers.

Example:

    // matches 'ab'
    /ab/

    // matches 'ab', 'AB', 'aB', or 'Ab'
    /ab/i

------

## Special Characters

There are several special characters you can use to denote different things in regex-land.

Example:

    . // match any valid character
    \d // match any digit character (0-9)
    \s // match any whitespace character (space, \t, or \n)
    \w // match any word character (A-Z, a-z, 0-9, and _)

    * // match 0 or more instances of the preceding character
    + // match 1 or more instances of the preceding character
    ? // match 0 or 1 instance of the preceding character

_Note: To match something like `.` or `*`, you need to “escape” the character using a backslash. E.g., `\.` or `\*`._

------

## Matching Ranges

You can specify ranges of characters to be matched.

Example:

    // match any of the digits 0 through 9
    [0-9]

    // match any uppercase letter from A to Z
    [A-Z]

    // match any lowercase letter from a to z or any digit 0 to 9
    [a-z0-9]

_Note: Because dashes are used to create ranges, to match a dash character, you need to escape it with a backslash. E.g., `\-`_

------

## Capturing Matches

You can “capture” matches or parts of matching patterns using parentheses.

Example:

    var matches = 'jane@doe.com'.match(/.*@(.*\..*)/);
    console.log('The hostname is ' + matches[1]);

------

Sources:

1. [Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
1. [Regular Expressions in JavaScript](https://www.sitepoint.com/expressions-javascript/)
