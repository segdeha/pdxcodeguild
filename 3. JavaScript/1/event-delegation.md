# Event Delegation

Event delegation is a technique whereby you can set an event listener on a parent element, but act on it as if the event event happened on a child element.

------

## Event Flow

### Capture Phase

JavaScript events propagate from the top of the tree down through the elements (called event “capturing”) until they reach the target element.

![Event capture phase](https://github.com/segdeha/pdxcodeguild/blob/master/3.%20JavaScript/assets/event-flow-capture.png?raw=true)

### Bubble Phase

Once an event reaches its target element, it then “bubbles” back up through the DOM tree.

![Event bubble phase](https://github.com/segdeha/pdxcodeguild/blob/master/3.%20JavaScript/assets/event-flow-bubble.png?raw=true)

One implication of the way events flow is that we can listen for an event at a higher level of the tree than the element we’re actually targeting.

------

## But, like, why?

Why would we want to do this? Everything in computing comes at a cost and event listeners are no exception.

Say you wanted to listen for the `hover` event on a group of 1000 list items. Attaching an event listener to each of the list items would be quite costly in terms of memory consumption and even CPU usage as the browser has to track interactions with so many DOM nodes.

Alternately, you could attach one event listener to the list, itself, then use the `target` property of the `Event` object to make changes to the element.

The difference may not be noticeable on most websites, but definitely results in a snappier UI on even moderately complex pages.

------

## How-to

Check out [this pen](http://codepen.io/segdeha/pen/aZZzjr) for an example implementation of event delegation. 

------

Sources:

1. [DOM events](https://en.wikipedia.org/wiki/DOM_events)
