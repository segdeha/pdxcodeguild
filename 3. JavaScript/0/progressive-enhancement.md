# Progressive Enhancement

Progressive enhancement is an approach to building web pages where you start with HTML, add CSS, then add JavaScript, and at each step the page is usable and accessible.

A plain, unstyled web page isn't pretty, but there’s no denying that any user using any user agent is going to be able to get to all of the content.

Add CSS to the HTML and it’s suddenly possible to make content invisible, push it off the screen, make the foreground and background colors the same, etc. In other words, with CSS, you can make your pages completely unusable, if you wanted to.

With JavaScript on the page, all bets are off regarding accessibility. JavaScript is capable of completely rewriting the page. It can also do less severe operations on the page that could potentially render content unusable or even unavailable.

The common mistake developers make with respect to CSS and JavaScript is to think that all users are going to have these technologies enabled. Users have the ability to override any CSS you put on the page. Users also have the ability to turn JavaScript off altogether.

Progressive enhancement tells us we should not make assumptions, especially about the presence of JavaScript. Make sure the page looks and works correctly (i.e. delivers all of the content, forms and links work, etc.), then add bells and whistles, upgrades, etc. for users who do have JavaScript enabled.
