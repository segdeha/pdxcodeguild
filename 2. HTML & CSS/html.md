# HTML

HTML stands for HyperText Markup Language. It was invented by [Sir Tim Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee) who was working at [CERN](http://home.cern), the European Organization for Nuclear Research, and wanted a way to share scientific papers among the scientists there.

------

HTML (the specification) describes a set of “tags” that can be used to add semantic infromation to the content of web pages.

Example:

    <h1>My Headline</h1>
    <p>This is my awesome paragraph of text.</p>

In the example above, `<h1></h1>` is a **header** tag. The text, `My Headline`, is the content. `<p></p>` is a **paragraph** tag. The text, `This is my awesome paragraph of text.`, is the content.

Most (but not all!) tags are structured like this, with an **opening** and **closing** tag.

In HTML documents, web browsers treat any number of consecutive whitespace characters (spaces, newlines, and tabs) as a single space. Because of this behavior, if we didn’t include the tags around the content above, it would render like the following:

    My Headline This is my awesome paragraph of text.

It’s the tags that tell the browser to render our example like the following:

------

# My Headline

This is my awesome paragraph of text.

------

## Moar Tags

HTML has tags for a bunch of useful and common semantics.

------

### Headers

HTML describes 7 levels of headers. This is a remnant from the original use case of scientific papers.

    <h1>My Headline</h1>
    <h2>My Sub-Headline</h2>
    <h3>My Sub-Sub-Headline</h3>

This renders as:

# My Headline
## My Sub-Headline
### My Sub-Sub-Headline

------

### Lists

The following describes an un-ordered list:

    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>

This renders as:

- Item 1
- Item 2
- Item 3

The following describes an ordered list:

    <ol>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ol>

This renders as:

1. Item 1
1. Item 2
1. Item 3

------

### Links

Links are what makes the web a web.

    <a href="http://example.com">Go to a super cool site</a>

This is our first example of a tag with an attribute.

- The tag is `<a></a>`
- The attribute is `href=""`
- The value for the `href` attribute is `http://example.com`

------

### Images

Without the `<img>` tag, it would be a whole lot harder to share cat GIFs.

    <img src="creeper-cat.gif" alt="Creeper Cat">

The above renders as follows:

![Creeper Cat](https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr06/anigif_enhanced-27866-1446482550-28.gif)

_Note: This is one of the tags in HTML that does not require a closing tag. I.e. there is no such thing as `</img>`._

The `<img>` tag takes a minimum of the following 2 attributes:

- `src` — Relative or fully-qualified URL to an image resource (GIF, JPG, PNG, SVG, BMP, ICO)

------

### Document structure

There are a few tags you can use to describe your document’s high-level structure. These typically don’t add styling information to the content.

Example:

    <div></div> <!-- generic container for content -->
    <section></section> <!-- generic section of content -->
    <article></article> <!-- self-contained piece of the document -->

These each have intended uses, but in a lot of cases can be used interchangeably.

The following tags describe sub-sets of the content:

    <aside></aside> <!-- content tangential to main content -->
    <figure></figure> <!-- container for an image, diagram, or code snippet; usually with a caption -->

------

### Comments

Similar to Python, you can add comments to HTML code. HTML comments are structured like the following:

    <!-- this is a comment -->
    
    <!-- this is a 
         multi-line comment -->

------

Sources:

1. [HTML5](https://www.w3.org/TR/html5/) (the official spec)
1. [Supported image formats](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#Supported_image_formats) from Mozilla Developer Network