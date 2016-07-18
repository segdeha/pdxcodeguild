# Django

Django is a popular [web application framework](https://www.fullstackpython.com/web-frameworks.html) built in Python. It was created in 2003 by [Simon Willison](https://en.wikipedia.org/wiki/Simon_Willison) and [Adrian Holovaty](https://en.wikipedia.org/wiki/Adrian_Holovaty), the latter of whom plays gypsy-jazz guitar and is a big fan of [Django Reinhardt](https://www.youtube.com/watch?v=PQhTpgicdx4) (video).

------

## What is a web application?

A web application is a site hosted on the web that offers significant functionality beyond simple, static pages. They often allow users to log in and save their work and are usually connected to a database of some kind. [Amazon](http://amazon.com), [LinkedIn](http://linkedin.com), and [Trello](http://trello.com) are all examples of web applications.

------

## What is a web application framework?

Web application frameworks make it easier to write web applications by providing simple ways to build common functionality including the following:

- Authentication
- Routes
- Models
- Views/templates
- Plugin architecture

------

## What does Django do for me?

The Django framework follows a “batteries included” philosophy. What this means is that the functions common to web applications are built-in to the framework rather than requiring external code (usually called plugins).

Some of the features of Django include the following:

- a lightweight and standalone web server for development and testing
- a form serialization and validation system that can translate between HTML forms and values suitable for storage in the database
- a template system that utilizes the concept of inheritance borrowed from object-oriented programming
- a caching framework that can use any of several cache methods
support for middleware classes that can intervene at various stages of request processing and carry out custom functions
- an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals (often called “hooks” in other frameworks)
- an internationalization system, including translations of Django's own components into a variety of languages
- a serialization system that can produce and read XML and/or JSON representations of Django model instances
- a system for extending the capabilities of the template engine
an interface to Python's built in unit test framework
- an extensible authentication system
- the dynamic administrative interface
- tools for generating RSS and Atom syndication feeds
- a sites framework that allows one Django installation to run multiple websites, each with their own content and applications
tools for generating Google Sitemaps
- built-in mitigation for cross-site request forgery, cross-site scripting, SQL injection, password cracking and other typical web attacks, most of them turned on by default[17][18]
a framework for creating GIS applications
