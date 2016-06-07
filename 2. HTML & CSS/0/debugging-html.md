# Debugging HTML

TBL made a decision when he invented HTML that it should be “permissive”. He wanted there to be as little friction as possible for people to be able to publish their content, so he intentionally made the language less strict than it could have been. This design decision seems to have paid off.

HTML being a permissive language is a double-edged sword. On one hand, it means your content is likely to be at least mostly usable/readable even if your markup is not perfect. On the other hand, it can be harder to find and fix problems in your markup because they won’t always show up as errors when you view your pages.

------

## Identifying Errors

Many errors in HTML are the result of one of the following:

- Forgetting the ending tag (e.g., leaving off `</a>`)
- A missing `"` on an attribute value (e.g., `<a href="foo>foo</a>`)
- A missing `<` or `>` on a tag (e.g., `<tr><td</td></tr>`)
- Incorrectly nested tags (e.g., `<em><strong></em></strong>`)

It can feel like you need eagle eyes to spot these kinds of mistakes! Luckily, the following are a couple of simple ways you can identify most of them pretty quickly:

1. Pay attention to the syntax highlighting in your text editor
1. [Validate your HTML](https://validator.w3.org)
