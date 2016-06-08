# CSS Box Model

The CSS specification, starting with version 1, has defined a box in CSS as having the following parts:

    ---------------------------------------------------
    |    Margin                                       |
    |   -------------------------------------------   |
    |   |   Border                                |   |
    |   |  -------------------------------------  |   |
    |   |  |    Padding                        |  |   |
    |   |  |   -----------------------------   |  |   |
    |   |  |   |                           |   |  |   |
    |   |  |   |         Content           |   |  |   |
    |   |  |   |                           |   |  |   |
    |   |  |   -----------------------------   |  |   |
    |   |  |   <---------- Width ---------->   |  |   |
    |   |  -------------------------------------  |   |
    |   |                                         |   |
    |   -------------------------------------------   |
    |                                                 |
    ---------------------------------------------------

The CSS `width` and `height` properties are used to set the dimensions of the **content** box. The **amount of space the box takes up on the page** is therefore the sum of the following:

- Computed values of the `width` and `height` properties
- Combined computed values of the `padding` property
- Combined computed thickness of any borders
- Combined computed values of the `margin` property

_Note: I say “computed” values here because you may specify any of these as, e.g., percentages, but they are translated to pixel values by the browser._

The following is an example showing how to set the values for various parts of the box model in CSS:

    div {
        width: 200px; /* content width */
        height: 100px; /* content height */
        padding: 10px;
        border: solid 2px black;
        margin: 20px;
    }

------

## Internet Explorer

The above is all fine and dandy these days. Every browser computes the width in accordance with the spec. This wasn’t always the case, however.

About 9 months after the [CSS1 spec](https://www.w3.org/TR/REC-CSS1/) was published, Microsoft released a new version of their web rendering engine, Trident, in [Internet Explorer 4](https://en.wikipedia.org/wiki/Internet_Explorer_versions#Microsoft_Internet_Explorer_4).

It didn’t follow the spec.

The following is how Microsoft decided to calculate the width of a box:

    ---------------------------------------------------
    |    Margin                                       |
    |   -------------------------------------------   |
    |   |   Border                                |   |
    |   |  -------------------------------------  |   |
    |   |  |    Padding                        |  |   |
    |   |  |   -----------------------------   |  |   |
    |   |  |   |                           |   |  |   |
    |   |  |   |         Content           |   |  |   |
    |   |  |   |                           |   |  |   |
    |   |  |   -----------------------------   |  |   |
    |   |  |                                   |  |   |
    |   |  -------------------------------------  |   |
    |   |                                         |   |
    |   -------------------------------------------   |
    |   <----------------- Width ----------------->   |
    ---------------------------------------------------

I.e. (pun intended) Microsoft calculated the **width & height** as the sum of the following:

- Computed values of the `width` and `height` properties
- Combined computed values of the `padding` property
- Combined computed thickness of any borders

Therefore, **the space the box takes up on the page** is the above plus the computed values of the `margin` property.

------

## Politics Over Engineering

It’s reasonably argued that Microsoft’s approach is more intuitive. However, the W3C at the time was a young organization and did not want to make it appear that they would just follow along with whatever Microsoft did.

So they stuck to the spec and Microsoft’s implementation was considered a [bug](https://en.wikipedia.org/wiki/Internet_Explorer_box_model_bug). It wasn’t until version 6 that you could render boxes in accordance with the spec in Internet Explorer. Even then, it was incredibly easy to code something slightly wrong and have the browser fall back to the euphemistically-named “quirks mode”.

Countless hours of many developers’ lives have been lost trying to [hack around this discrepancy in the box model](http://tantek.com/CSS/Examples/boxmodelhack.html).

> May you live in interesting times.

Indeed.

------

## CSS Brings Back Quirks Mode!

Around 2010, the W3C added the ability for developers to control which box model they use to the CSS spec. (Maybe the W3C no longer feels quite so threatened by the [Beast of Redmond](http://www.urbandictionary.com/define.php?term=Beast%20of%20Redmond)?)

The syntax to do this, if you ever care to, is as follows:

    div {
        box-sizing: border-box;
    }

The above CSS will change the box model for all `<div></div>` tags on your page. If you want to change how it works for all elements on your page, do the following:

    html {
        box-sizing: border-box;
    }
    *, *:before, *:after {
        box-sizing: inherit;
    }

The above CSS could simplify the calculation of widths in some cases. E.g., say you’re laying out some columns. The way `margin` works is that for boxes next to each other their margins will overlap. Calculating the correct width for your columns would be easier because you wouldn’t have to make adjustments to the widths if you, say, changed the padding.

------

Sources:

1. [Introduction to the CSS box model](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model/Introduction_to_the_CSS_box_model)
1. [The Box Model For Beginners](https://www.addedbytes.com/articles/for-beginners/the-box-model-for-beginners/)
1. [The Revenge of the IE Box Model?](https://www.jefftk.com/p/the-revenge-of-the-ie-box-model)
1. [* { box-sizing: border-box } FTW](http://www.paulirish.com/2012/box-sizing-border-box-ftw/)
