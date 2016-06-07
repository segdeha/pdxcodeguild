# How the Web Works

> What do you mean? Don’t you just Google for “amazon.com” and click the first link that it shows you?

Well, yes and no. That is a way to describe the end-user experience, but there is a lot going on under the hood to make it possible for you to buy that [Nicolas Cage pillow case](http://www.amazon.com/Nicolas-Signature-Custom-Pillowcase-Pillowslips/dp/B00NQWCC8W/ref=pd_bxgy_201_img_3?ie=UTF8&refRID=01AJ47PPXH9HKN5V8CJN).

## The Internet

The internet consists of all of the computers around the world (and [in space](http://www.theatlantic.com/technology/archive/2015/06/the-internet-in-space-slow-dial-up-lasers-satellites/395618/)!) that are connected to each other via a complex network of wires and radio waves controlled by specialized hardware called routers and switches.

Every device on the internet is assigned a unique identifier, known as an IP (Internet Protocol) address. When you enter “google.com” into your web browser, that name gets translated to an [IP address](https://support.google.com/websearch/answer/1696588) by specialized servers called [DNS](https://en.wikipedia.org/wiki/Domain_Name_System) (Domain Name System) servers.

The IP addresses you’re probably familir with look like `216.58.193.110` (that’s the IP address for google.com, by the way), where each number ranges from 0 to 255, for a total of 4,294,967,296 possible IP addresses.

These days, there are so many connected devices in the world that 4.2 billion addresses isn’t enough.

The internet is in the process of switching over to a new standard called IPv6 (the old one was IPv4). IPv6 addresses look like `2001:4860:4860::8888` (that’s the IPv6 address of one of [Google’s public DNS servers](https://developers.google.com/speed/public-dns/)). The new format allows for a total of 340,282,366,920,938,463,463,374,607,431,768,211,456 unique addresses. (That’s 340 [undecillion](https://en.wikipedia.org/wiki/Names_of_large_numbers), in case you’re curious.)

That should do us for a while.

## The Web

Repeat after me: **The web is not the internet.**

The web is one of many applications that sit on the internet infrastructure. Email is another. FTP, SSH, VPN, and countless other services are others. In the words of former U.S. Senator, Ted Stevens (R-Alaska), [the internet is a series of tubes](https://www.youtube.com/watch?v=_cZC67wXUTs). The web is just one thing that flows through these tubes.

The web consists of resources (text, images, audio, video) on servers that are reachable via [URLs](https://en.wikipedia.org/wiki/Uniform_Resource_Locator). If you want to go deeper, read up about [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol). The gist is that HTTP allows for [stateless](https://en.wikipedia.org/wiki/Stateless_protocol) request/response interactions between clients (usually web browsers) and servers.

## Web Browsers

Microsoft Edge, Internet Explorer, Google Chrome, Apple’s Safari, Opera, Firefox, these are all examples of web browsers. The job of a web browser is to **make requests** to web servers and **display the results.**

Up to just a few years ago, the various web browsers were super inconsistent in how they did this. The situation is better now, but there are still corners of the internet where these inconsistencies raise their ugly head (e.g., HTML emails).

## Web Servers

Web servers are just computers, connected to the internet, that understand requests from web browsers (and other HTTP clients) and know how to respond appropriately.

There are [approximately 1 billion websites](http://www.internetlivestats.com/total-number-of-websites/) online. Some servers serve many websites (sometimes called “shared hosting”) and some websites (e.g., www.facebook.com and www.google.com) are powered by 100s of 1000s of servers. The number of web servers in the world is likely on the order of 1 order of magnitude less than the number of sites, but don’t quote me on that.

## Anatomy of a Web Request

Every one of us has at some point typed `www.google.com` into our browser’s address bar and hit enter. How many of us know what actually happens next?

What’s actually happening under the hood is that the web browser first resolves the URL to an IP address, then crafts a complex string of text to send to the web server. 

This string of text is called an [HTTP packet](https://en.wikipedia.org/wiki/HTTP_message_body) and it consists mostly of [headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) related to the request, including the following:

- Whether it’s a secure request or not (`http` vs. `https`)
- The location of the resource being requested (e.g., if the URL entered is `http://example.com/search?q=lolcat`, the location would be `/search?q=lolcat`)
- The kind of request (e.g., `GET` or `POST` [we’ll cover this more in a future lesson])
- What [type](https://en.wikipedia.org/wiki/Media_type) of response the client is capable of accepting, including file types and acceptable compression schemes
- The preferred language (e.g., U.S. English) of the response
- Any [cookies](https://en.wikipedia.org/wiki/HTTP_cookie) for the domain entered
- An optional body of content (used usually in conjunction with `POST` requests)
- The [user agent string](https://en.wikipedia.org/wiki/User_agent) (a string of text that is supposed to help the web server identify what browser is being used to make the response, but is so easily spoofable and so often misused that it’s basically worthless)

Did you have any idea so much went into those visits to [dilbert.com](http://www.dilbert.com)?

To be fair, all of the above isn’t strictly required to make an [HTTP request](http://stackoverflow.com/questions/6686261).

## Anatomy of a Web Response

Web servers respond to correctly formatted requests with the following information:

- An [HTTP status code](https://http.cat/) (there are a bunch of these, but some of the common ones are `200` for a successful response, `404` for a missing resource, and `500` for a server error)
- Response headers, including the version of HTTP being served (`1.0` or `1.1`) the content [type](https://en.wikipedia.org/wiki/Media_type), the date and time of the response, and other optional information such as whether the response was served from cache
- The body of the response (this is usually the content that we’re most interested in)

The body of the response can be text (e.g., HTML), an image, video, audio, or anything else that can be transmitted as 1s and 0s across wires and airwaves.

------

Sources:

1. [Anatomy of a Web Request](https://robrich.org/slides/anatomy_of_a_web_request/)
