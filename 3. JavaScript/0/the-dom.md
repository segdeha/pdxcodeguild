# The DOM

The Document Object Model (DOM) is both a representation of and a set of JavaScript APIs for interacting with elements of an HTML page.

## It’s a tree.

![HTML describes a tree of elements](http://www.teaching-materials.org/jsweb/slides/domtree.png)

_Diagram from [teaching-materials.org](http://www.teaching-materials.org/)_

HTML describes a tree of elements. At the root of the tree is the `<html></html>` element. The JavaScript object `document` contains a reference to the `<html></html>` element as well as methods for traversing the tree.

### Mini-exercise: Inspect the document object

1. Open the web inspector by right-clicking and choosing `Inspect` or `Inspect Element`
1. Type `document` into the console and hit [enter]
1. Open up the result to see the HTML tree underneath
1. Copy and paste the following into the console, then hit [enter]:
    
    ```for (var p in document) { console.log(p, document[p]) }```

1. Observe the results

------

## Selecting Elements

There are several ways to select elements from the DOM. We are not going to cover all of them, only the most useful.

Example:

    var el = document.getElementById('my-id');
    var el = document.querySelector('#my-id');

The above statements are equivalent. They both select the HTML element with the `id` attribute with the value `my-id` from the DOM. Both take a string as the sole argument and return either a “DOM node” or `null` if there is no match.

### Mini-exercise: Select an element

1. Open the web inspector by right-clicking and choosing `Inspect` or `Inspect Element`
1. Type `var el = document.querySelector('body');` and hit [enter]
1. Copy and paste the following into the console, then hit [enter]:
    
    ```for (var p in el) { console.log(p, el[p]) }```

1. Observe the results

DOM elements have [many specialized methods](https://developer.mozilla.org/en-US/docs/Web/API/Node). We’ll learn about a few of the most useful ones in future lessons.

------

You can also select multiple elements from the page in a single go.

Example:

    var els = document.querySelectorAll('ul a');

The above will select all `<a></a>` tags that are children of a `<ul></ul>` tag.

What’s returned by `querySelectorAll` is what’s called a “NodeList”. It’s similar to an array, but lacks most array methods. Luckily, a NodeList still has `forEach` so you can easily loop over its contents.

### Mini-exercise: Select several elements

1. Open the web inspector by right-clicking and choosing `Inspect` or `Inspect Element`
1. Type `var els = document.querySelectorAll('p');` and hit [enter]
1. Copy and paste the following into the console, then hit [enter]:
    
    ```for (var p in els) { console.log(p, els[p]) }```

1. Observe the results

------

## Useful DOM Methods & Properties

Some of the common things you might want to do with a DOM element once you select it include the following:

- Change the class names assigned to it
- Add or remove an event listener

------

Sources:

1. [Document Object Model](https://en.wikipedia.org/wiki/Document_Object_Model) on Wikipedia
1. [Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) on Mozilla Developer Network
