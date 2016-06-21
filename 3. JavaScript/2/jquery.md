# jQuery

[jQuery](http://jquery.com/) was first published in 2006 by [John Resig](http://ejohn.org/). Around [74% of the 1M most popular websites](https://trends.builtwith.com/javascript/jQuery) use jQuery.

jQuery was written at a time when web browsers were very inconsistent and buggy in their implementations of then nascent standards. Resig wrote the library with two goals in mind:

1. To simplify working with the DOM
1. To reduce the number of cross-browser issues that would need to be addressed when developing web pages.

jQuery quickly grew to do much more including the following:

- Use CSS selectors to select elements (this was before `querySelector` existed!)
- Provide a consistent interface for setting and reacting to events
- Provide a consistent interface for making Ajax calls and handling their responses
- Set arbitrary CSS on elements
- Measure the dimensions of elements on the page (harder than you might think!)
- Animate elements on the page

When he wrote jQuery, Resig did two things that were pretty brilliant for 2006 and contributed to its rapid adoption:

1. Leveraged chaining to simplify working with DOM elements
1. Provided a plugin API so people could extend jQuery with isolated pieces of code (there are some [seriously cool plugins](http://www.creativebloq.com/jquery/top-jquery-plugins-6133175) out there)

The jQuery project also published [jQuery Mobile](http://jquerymobile.com/), one of the first and most complete mobile JavaScript frameworks, and [jQuery UI](https://jqueryui.com/), a robust set of UI widgets you can use in your pages.

------

## Examples

Selecting elements:

    $('h1')
    $('ul li:first-child')
    $('#menu .item > a')

Fade in an element:

    $('.hidden').fadeIn();

Animate an element from left to right:

    $('h1').animate({
        left: '+=100'
    });

Change some CSS:

    $('h1').css({
        color: 'red'
    });

Chain several operations:

    $('.hidden')
        .fadeIn()
        .animate({
            left: '+=100'
        })
        .css({
            color: 'red'
        })
    ;

Set an event handler:

    $('h1').click(function () {
        alert('I was clicked!');
    });

Make an [Ajax](https://developer.mozilla.org/en-US/docs/AJAX/Getting_Started) request:

    $.ajax({
        url: 'http://example.com'
    })
    .done(function (data) {
        alert(data);
    });

------

Sources:

1. [Official jQuery Documentation](http://jquery.com/)
1. [jQAPI - Alternative jQuery Documentation Browser](http://jqapi.com/)
1. [jQuery Mobile](http://jquerymobile.com/)
1. [jQuery UI](https://jqueryui.com/)
