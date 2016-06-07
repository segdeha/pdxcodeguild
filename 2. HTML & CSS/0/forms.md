# Forms

HTML forms are what allows us to collect information from users, enabling customized experiences.

[There is a lot to forms](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms), but we’ll try to keep it relatively simple for now.

------

## Forms Syntax

Betcha can’t guess what the tag is for a form…. If you guessed `<form></form>`, you would be correct. The `<form></form>` tag takes a minimum of two attributes: `method` and `action`.

- `action` — The URL to which the form will be submitted
- `method` — Describes the type of request to be made, either `GET` or `POST` (**never** use `GET` with a form involving sensitive information, such as passwords!)

------

Forms consist of one or more of various types of form fields including text inputs, radio buttons, checkboxes, select lists, and buttons. Each has specific uses. _Be careful to use form fields as intended, otherwise you’re likely to throw off your users!_

------

### Text inputs

There are two common types of text inputs: plain text and passwords. It is also possible to designate text inputs as numbers, telephone numbers, email addresses, dates, and other specific foramts. The specialized types of text inputs aren’t widely supported yet, but you can use them safely because they will fallback to being plain text inputs on browsers where they’re not supported.

Examples:

    <input type="text" name="my-text">
    <input type="password" name="my-password">
    <input type="tel" name="my-telephone-number">

Another type of text input, called a textarea, exists for multi-line input.

Example:

    <textarea name="my-long-text"></textarea>

_Notice that this tag, unlike the `<input>` tag, takes a closing tag._

------

### Checkboxes

Checkboxes are used when you want to allow the user to make an “on/off” style decision or have them select several out of a group of options.

Example:

    <input type="checkbox" name="agree-to-terms"> Agree to terms?

Example:

    <p>Select your interests from the options below:</p>
    <input type="checkbox" name="interests" value="volleyball"> Volleyball
    <input type="checkbox" name="interests" value="disc-golf"> Disc Golf
    <input type="checkbox" name="interests" value="mtb"> Mountain Biking
    <input type="checkbox" name="interests" value="camping"> Camping

_Note: When several checkboxes share the same name, their data will be sent to the server as a group. **Only checked checkboxes will be included!**_

------

### Radio buttons

Radio buttons are used to allow the user to choose exactly one item from a group of two or more options.

Example:

    <p>Select our favorite day of the week:</p>
    <input type="radio" name="fav-day" value="sun"> Sunday
    <input type="radio" name="fav-day" value="tue"> Tuesday
    <input type="radio" name="fav-day" value="wed"> Wednesday
    <input type="radio" name="fav-day" value="thu"> Thursday
    <input type="radio" name="fav-day" value="fri"> Friday
    <input type="radio" name="fav-day" value="sat" checked> Saturday

_Notice that the radio buttons above all share the same name. This is what tells the browser to restrict the user to choosing only one of the set._

_Also notice above that the input for Saturday includes the `checked` attribute. This specifies to the browser that this value is checked by default._

------

### File inputs

File inputs allow the user to select a file from their filesystem to be uploaded when the form is submitted.

Example:

    <p>Select a goofy photo to upload:</p>
    <input type="file" name="goofy-photo">

------

### Select lists

Also known as “drop downs,” by default select lists allow users to select one item from a list of options.

Example:

    <select name="state-in-the-pnw">
        <option value="ID">Idaho</option>
        <option value="OR">Oregon</option>
        <option value="WA">Washington</option>
    </select>

Select lists can take the optional `multiple` attribute that allows the user to select multiple options.

Example:

    <select multiple name="favorite-cuisines">
        <option>Indian</option>
        <option>Italian</option>
        <option>Mexican</option>
        <option selected>Thai</option>
    </select>

_Notice that I didn’t specify the `value` attribute above. If omitted, the value will be the content inside the `<option></option>` tag._

_Also notice that above the tag for Thai includes the `selected` attribute. This tells the browser to select that option by default._

------

### Buttons

Buttons are used to submit forms. The new, standard way to render a button is as follows:

    <button>Submit</button>

In older code, you may see the following:

    <input type="submit" value="Submit">

------

### Labels

It’s good form (har har) to put a `<label></label>` tag around your form fields. This improves the user experience by allowing the user to click on the label text to select the form field.

Example:

    <label>
        <input type="checkbox" name="newsletter"> Receive newsletter?
    </label>
