# Bugs

![Actual case of bug being found](http://www.extremities.com/pct/hwbasics/images/mark2bug.jpg)

In your first developer job, it’s highly likely that one of the first tasks you’ll be given is to fix bugs in an existing codebase.

This is an opportunity!

Fixing defects in existing software is a great way to learn your way around a complex codebase and feel like a champion when you finally track down and squash that pesky bug.

------

## Bug Reports

Bug reports are typically tracked in some kind of bug tracking system and can come from one of a few sources:

- End users (often via email)
- A quality assurance (QA) team
- Developers as they’re working on and using the software
- The CEO (fix these ones first; I’m only kind of kidding)

------

Good bug reports include enough detail for you, as the developer, to be able to reproduce the problem. _If you can’t reproduce it, you have no way to know whether you fixed it!_

Some organizations go as far as to publish [guidelines for submitting bugs](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines) in an attempt to gather the right information.

When writing bugs, try to include the following:

- Clear, concise summary of the problem
- Observed behavior
- Expected behavior
- Steps to reproduce
- Any other important details (e.g., browser version, OS, etc.)

------

Example:

> **Summary:**
> When uploading an image, I get an error even though the guidelines say it should work.
>
> **Observed behavior:**
> The system reported the error “File type not supported”.
>
> **Expected behavior:**
> The image should upload successfully.
>
> **Steps to reproduce:**
> 1. Go to http://example.com/upload-image/
> 2. Click the button “Upload Image”
> 3. Select a PNG from the filesystem
> 4. Click the button “OK”
>
> **Other details:**
> I’m on OS X 10.11.4 using Chrome version 50.0.2661.102.
