# Events

JavaScript events are what allow us to give web pages interactivity. You add events to DOM elements using the `addEventListener` method.

Example:

    document.getElementById('my-div')
        .addEventListener('click', function (evt) {
        console.log('The DIV was clicked.');
    });

## Mouse Events

Events the user triggers with a mouse (or trackball) include the following:

- `click`
- `mouseover`
- `mousedown`
- `mouseup`
- `mouseout`
- `dblclick`
- `mouseenter`
- `mouseleave`

------

## Touch Events

Touch events are a bit more complicated than mouse events. Some of them are similar. Consider the following:

- `touchstart`
- `touchend`
- `touchcancel`
- `touchmove`

_Note: There is no native `tap` event, but you could argue there should be!_

It gets complicated fast when you start to talk about multi-touch. We’ll skip over that topic for now. If you want to dive deeper, [start here](http://www.html5rocks.com/en/mobile/touch/).

------

## Keyboard Events

The following keyboard events are generated when the user types on either a physical or software keyboard:

- `keydown`
- `keypress`
- `keyup`

When handling a keyboard event, you can test for whether a modifier key was being pressed at the same time by testing the following either `true` or `false`:

- `KeyboardEvent.ctrlKey`
- `KeyboardEvent.shiftKey`
- `KeyboardEvent.altKey` ([option] on a Mac)
- `KeyboardEvent.metaKey` ([cmd] on a Mac)

You’re also able to test which key was pressed by evaluating `KeyboardEvent.code` against [this list of codes](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/code).

Example:

    window.addEventListener('keyup', function (evt) {
        if (evt.code === 'KeyA') {
            console.log('The A key was pressed.');
        }
    });

------

Sources:

1. [Event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
1. [Touch events](https://developer.mozilla.org/en-US/docs/Web/API/Touch_events)
