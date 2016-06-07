# CSS

Cascading Style Sheets (CSS) provides presentation to HTML’s structure. It’s like the icing on a cake. Mmm…cake.

------

CSS looks like the following:

    h1 {
        color: red;
        font-size: 48px;
    }

Let’s break down the above example.

- `h1` is a **selector,** an _element_ selector, to be specific
- The lines inside the curly braces are the CSS **rules**
- `color` and `font-size` are examples of **properties**
- `red` and `48px` are examples of **values**

------

## Default Styles

Those simple pages you’ve made so far? No CSS, right? _Actually,_ your web browser added CSS rules behind the scenes. Try this:

1. Open the first page you made yesterday
1. Open the Web Inspector to allow you to peek behind the curtain
1. Click on any element inside the `<body></body>` tag
1. Check out the style rules applied to it in the “Styles” tab of the web inspector

------

## What can CSS do?

CSS can be used to do the following (not an exhaustive list!):

- Add color
- Change typography
- Change the size of elemnts
- Make things look 3D
- Set layout
- Animate elements
- Add content to pages
- Create [blinking Simpsons character faces](http://pattle.github.io/simpsons-in-css/)
- Change any of the above based on the size of the viewport

------

## How do you add CSS to a web page?

There are a few ways you can apply CSS to your web pages, presented here in descending order by desirability.

    <!-- link to an external style sheet -->
    <link rel="stylesheet" href="styles.css">

    <!-- add a style block to the head of your
         HTML document -->
    <style type="text/css">

    /* styles go here */

    </style>

    <!-- add styles directly to elements via the
         `style` attribute (try to avoid this!) -->

Linking to an external style sheet is by far the best practice in most cases. It allows the browser to cache your CSS file so it can be re-used across multiple pages without making more network requests.

Adding a style block to the `<head></head>` of your document works, but means that the styles can’t be cached independent of your page. There are times when, for performance reasons, you may want to put [critical CSS](https://www.smashingmagazine.com/2015/08/understanding-critical-css/#what-is-critical-css) in a style block and still link to an external style sheet that contains the bulk of your CSS.

Inline styles (styles added directly to elements via the `style` attribute) are nearly impossible to override. Avoid doing this unless you really know what you’re doing.
