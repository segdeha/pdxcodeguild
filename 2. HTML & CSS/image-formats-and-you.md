# Image Formats & You

There are several image formats that work on the web, but they are not created equal. The various formats have their strengths and weaknesses. Here, we will learn which to use in which situations.

------

## GIF

Extension: `.gif`

Introduced by CompuServe in 1987, [GIF](https://en.wikipedia.org/wiki/GIF) images are incredibly common on the web. They can also be animated, as anyone with a web browser knows, however much to their chagrin.

![I have no words.](http://i.imgur.com/8K7aWbG.gif)

GIFs compress really well for flat color art. They also have the ability to set part of the image as transparent (called an “alpha channel”). GIF is what’s called a “lossless format”. That means you can save a GIF with the same settings repeatedly and not lose any image information.

Their biggest downsides of GIF are that they are limited to 256 colors and that their alpha channel is binary (on or off, only).

------

## JPEG

Extensions: `.jpg`, `.jpeg`

[JPEG](https://en.wikipedia.org/wiki/JPEG) (which stands for Joint Photographic Experts Group) is the preferred delivery format for photographs and images with gradients due to the its ability to compress large, complex images to small filesizes.

![JPEG showing decreasing compression from left to right](https://upload.wikimedia.org/wikipedia/commons/e/e9/Felis_silvestris_silvestris_small_gradual_decrease_of_quality.png)

The major downside of JPEG is that it’s a “lossy” format. That is, if you were to save the same image at the same compression settings repeatedly, you would lose image information each time.

------

## PNG

Extension: `.png`

Like GIF, [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) is a “lossless” format. That means that no image information is lost when the image is compressed. This makes it good for delivering highly accurate representations of content.

For example, most product images on [www.apple.com](http://www.apple.com) are PNGs. One of their advantages is that they provide an [alpha-channel](https://en.wikipedia.org/wiki/Alpha_compositing) which allows you to set certain parts of the image as transparent.

Their downside is filesize. A high-quality PNG is going to be around 5× the filesize of the equivalent JPEG (approximately, depending on the JPEG compression settings), though PNGs are usually smaller than their equivalent GIFs.

### PNG8

The PNG8 format (the “8” stands for the fact it stores 8 bits of information per pixel) is similar to GIF in that they both allow a maximum of 256 (i.e. 2^8) colors. The main advantage of PNG8 over GIF is that it is not patent encumbered.

### PNG24

PNG24 (the “24” stands for 24-bit, though in reality it stores up to 64 bits of information per pixel in certain configurations) provides full-color and lossless compression. Its main downside is large filesizes.

_Note: This isn’t as much of a concern these days, but versions 4 through 8 of Internet Explorer had a [variety of problems](https://en.wikipedia.org/wiki/Portable_Network_Graphics#Web_browser_support_for_PNG) correctly rendering PNGs._

![iPhone SE image from apple.com](http://images.apple.com/v/iphone-se/a/images/overview/technology_static_large.png)

------

## SVG

Extension: `.svg`

[SVG](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) stands for Scalable Vector Graphics. Unlike the other formats, which are [raster](https://en.wikipedia.org/wiki/Raster_graphics) formats, SVG is a [vector](https://en.wikipedia.org/wiki/Vector_graphics) format. What this means is that you can scale an SVG up or down and its edges will stay equally sharp because rather than storing information about what color each pixel should render it stores information about lines and curves.

SVG as a format has been around since 1999, but it’s only really seen widespread adoption in the last couple of years as [browser support](http://caniuse.com/#search=svg) finally became more or less uniform.

As a vector format, SVG filesizes can be truly tiny for simple shapes and flat-color art and gradients (e.g., website icons). It’s not well-suited for photographic content.

![Darth Vader](http://thecraftchop.com/files/images/darth_1.svg)

------

## ICO

Extension: `.ico`

Browsers look for what’s called a [favicon](https://en.wikipedia.org/wiki/Favicon) when they visit a new website. These are tiny images that are used to represent the site in the navigation bar. They can be created in either BMP, GIF, or PNG formats.

------

## BMP

Extension: `.bmp`

Don’t use BMP for anything other than a favicon. It offers no advantage over other formats and the filesizes are huge.
