# Exercise: Is it a vowel?

## Objective

Get familiar with basic JavaScript constructs by writing a program that prompts the user for a character and tells them whether or not it’s a vowel.

1. Create a new file called `vowels.html` based on [this template](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/2.%20HTML%20%26%20CSS/solutions/structure-with-inline-css-and-javascript.html?token=AAAQ0sNxHlhyXhaAZLGeWybrKtZIAd68ks5XZzmgwA%3D%3D)
1. Add your JavaScript inside the `<script></script>` tag
1. To run your program, you will need to load `vowels.html` in a web browser

------

## Helpful hints

#### prompt

Use the built-in function `prompt` to ask the user for input. The result of `prompt` should be assigned to a variable.

Example:

    var input = prompt('Enter a character');

#### alert

Use the built-in function `alert` to tell the user the result.

Example:

    alert('The character you entered is a vowel');

#### indexOf

Similar to the `index` method on Python lists, JavaScript arrays have a method called [indexOf](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf) that returns the array index of the value or `-1` if the value is not present.

Example:

    ['a'].indexOf('a') // 0
    ['a'].indexOf('b') // -1

You could use the `indexOf` method to detect whether the user’s input is one of the items in an array of vowels.

------

## Extra Credit

- Handle upper and lower case input
- Handle the case of `y`
- Handle common accented characters (consider using the [charCodeAt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charCodeAt) method and this [reference of character codes](https://en.wikipedia.org/wiki/ISO/IEC_8859-1#Codepage_layout))
- Write your program in such a way that the user will continue to be prompted until they enter an empty string
