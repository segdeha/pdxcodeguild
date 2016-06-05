# HTML

HyperText Markup Language (HTML) was invented by [Sir Tim Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee) who was working at [CERN](http://home.cern), the European Organization for Nuclear Research, and wanted a way to share scientific papers among the scientists there.

------

## How Tags Work

[HTML](https://www.w3.org/TR/html5/) describes a set of “tags” that can be used to add [semantic infromation](https://en.wikipedia.org/wiki/Semantic_HTML) to the content of web pages.

Example:

    <h1>My Headline</h1>
    <p>This is my <em>awesome</em> paragraph of text.</p>

In the example above, `<h1></h1>` is a **header** tag. The text, `My Headline`, is the content.

Likewise, `<p></p>` is a **paragraph** tag. The text, `This is my awesome paragraph of text.`, is the content.

The `<em></em>` tag adds **emphasis** to the word “awesome” in our sentence.

Most tags (with a few exceptions) are structured like this, with an **opening** and **closing** tag.

In HTML documents, web browsers treat any number of consecutive whitespace characters (i.e. spaces, newlines, and tabs) as a single space. Because of this behavior, if we took out the tags around the content above, it would render like the following:

    My Headline This is my awesome paragraph of text.

It’s the tags that tell the browser to render our example like the following:

------

# My Headline

This is my _awesome_ paragraph of text.

------

## Moar Tags

HTML provides tags for a host of common semantics. These give the content structure and meaning. Always try to [find and use a semantic tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) if one is available for what you’re trying to convey.

------

### Headers

HTML describes 6 levels of headers (`<h1>`, `<h2>`, … `<h6>`). This number of headers is a remnant from the original use case of scientific papers, but it’s adequate for most situations.

Example:

    <h1>My Headline</h1>
    <h2>My Sub-Headline</h2>    
    <h3>My Sub-Sub-Headline</h3>

Web browsers render the above as follows:

# My Headline
## My Sub-Headline
### My Sub-Sub-Headline

------

### Paragraphs

The `<p></p>` tag might be the most common tag on the web. It is used to contain a paragraph of text.

Example:

    <p>
        This is my paragraph of text. It is my
        favorite because I wrote it. I can make
        it as long as I want.
    </p>

Web browsers render the above as follows:

This is my paragraph of text. It is my favorite because I wrote it. I can make it as long as I want.

------

### Emphasis

There are two levels of emphasis you can add to words in HTML: _emphasis_ and **strong emphasis.**

Example:

    <em>Usually rendered as italics</em>
    <strong>Usually rendered as bold</strong>

Web browsers render the above as follows:

_Usually rendered in italics_ **Usually rendered as bold**

------

### Lists

The following describes an **un-ordered list:**

    <ul>
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
    </ul>

Web browsers render the above as follows:

- Item A
- Item B
- Item C

The following describes an **ordered list:**

    <ol>
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
    </ol>

Web browsers render the above as follows:

1. Item A
1. Item B
1. Item C

------

### Links

Links are what makes the web a web.

    <a href="http://example.com">
        Go to my super cool site
    </a>

Web browsers render the above as follows:

[Go to my super cool site](http://example.com)

This is our first example of a tag with an attribute.

- The **tag** is `<a></a>`
- The **attribute** is `href=""`
- The **value** for the `href` attribute is `http://example.com`

_Note: There are several tags that require certain attributes to be useful. For now, just understand that attributes allow us to set values that are used by the web browser to affect the rendering and functionality of certain tags._

------

### Images

Without the `<img>` tag, it would be a whole lot harder to share cat GIFs. [#truth](https://twitter.com/search?q=%23truth)

    <img src="creeper-cat.gif" alt="Creeper Cat">

Web browsers render the above as follows:

![Creeper Cat](https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr06/anigif_enhanced-27866-1446482550-28.gif)

_Note: This is one of the tags in HTML that does not require a closing tag. I.e. there is no such thing as `</img>`._

The `<img>` tag **requires** the following 2 attributes:

- `src` — Relative or fully-qualified URL to an image resource of one of the following types: GIF, JPG, PNG, SVG, BMP, ICO
- `alt` — Alternative text for the image that will be read by screen readers

_Note: It may be appropriate to leave it empty if the image is purely decorative, but you **always** need to include the `alt` attribute in your `<img>` tags!_

Images are sometimes put in `<figure></figure>` containers when they are intended to convey some important content, such as a chart or code snippet. In those cases, they will usually be coupled with a `<figcaption></figcaption>` element that provides a textual description of the illustration.

Example:

    <figure>
        <img src="creeper-cat.gif" alt="Creeper Cat">
        <figcaption>
            <p>Creepy cats are creepy.</p>
        </figcaption>
    </figure>

------

### Comments

Similar to Python, you can add comments to HTML code. HTML comments are structured like the following:

    <!-- this is a comment -->
    
    <!-- this is a 
         multi-line comment -->

------

### Content structure

There are a few tags you can use to describe your content’s high-level structure. These typically don’t add much in the way of styling information.

Example:

    <!-- self-contained piece of the document -->
    <article></article>

    <!-- container for a section of content -->
    <section></section>

    <!-- generic container for content -->
    <div></div>

Each of the above has an intended use, but in practice these tags can often be used interchangeably.

HTML provides specific tags for common semantics related to headers, navigation, and footers on a web page.

Example:

    <header>
        <h1>My Page’s Header</h1>
        <nav>
            <!-- nav links go here -->
        </nav>
    </header>

    <footer>
        <p>My page’s footer.</p>
    </footer>

Additionally, the following tags describe sub-sets of the content:

    <!-- content tangential to main content -->
    <aside></aside>

    <!-- container for an image, diagram, or code snippet
         usually with a caption -->
    <figure></figure>

Putting all of these together, the content for a page might be structured something like the following:

    <article>
        <header>
            <h1>My Page’s Header</h1>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact Us</a></li>
                </ul>
            </nav>
        </header>
        <section>
            <h1>Section 1 Header</h1>
            <aside>
                <p>Something tangential</p>
            </aside>
            <p>Some content</p>
        </section>
        <section>
            <h1>Section 2 Header</h1>
            <figure>
                <img src="diagram.png" alt="Diagram showing something important">
                <figcaption>
                    <p>Something important is happening here</p>
                </figcaption>
            </figure>
            <p>Some more content</p>
        </section>
        <footer>
            <p>Copyright 2016, PDX Code Guild. All rights reserved.</p>
        </footer>
    </article>

------

Sources:

1. [HTML5](https://www.w3.org/TR/html5/) (the official spec)
1. [Supported image formats](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#Supported_image_formats) from Mozilla Developer Network
1. [HTML element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element) from Mozilla Developer Network
