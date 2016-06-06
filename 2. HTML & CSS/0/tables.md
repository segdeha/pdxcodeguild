# Tables

Remember how I said that the web was invented to help scientists share information? A big part of what scientists share is their research results and a big part of that is giant, boring tables of data.

Consequently, HTML has tags that can be used to describe giant, boring tables of data.

Somewhere along the line, before CSS was really a thing, people decided to use tables to give web pages fancy layouts. Thankfully, those days are behind us and tables are, again, relegated to displaying tabular data.

Tables are basically like spreadsheets. They consist of rows and columns and cells. You can designate cells as headers. You can also merge cells across rows or columns (but not both at once!).

## Table Syntax

It all starts, unsurprisingly, with the `<table></table>` tag.

The `<table></table>` tag is not a direct container for content. There are a few tags that are legal to put inside the `<table></table>` tag, but we’re going to keep it simple and focus first on the tag for a row: `<tr></tr>`.

The `<tr></tr>` is also not a direct container for content. That job is left to table cells. Table cells are, in fact, the only tags that are allowed to be the direct descendents of the `<tr></tr>` tag.

There are two types of table cells, headers cells and non-header cells. Header cells are designated using the `<th></th>` tag. Non-header cells are designated using the `<td></td>` tag.

Example:

    <table>
        <tr>
            <th>I am a header</th>
            <td>I am not a header</td>
        </tr>
    </table>

The above is a super simple table consisting of one row and two cells, one of which is a header.

------

We can add more rows and more cells, but we need to keep the grid consistent. That is, if one row has X number of cells, all rows should have that same number of cells.

Bad example:

    <table>
        <tr>
            <th>I am a header</th>
            <td>I am not a header</td>
            <td>I am a 3rd column</td>
        </tr>
        <tr>
            <th>I am a header in the 2nd row</th>
            <td>I am not a header in the 2nd row</td>
        </tr>
    </table>

Better example:

    <table>
        <tr>
            <th>I am a header</th>
            <td>I am not a header</td>
            <td>I am a 3rd column</td>
        </tr>
        <tr>
            <th>I am a header in the 2nd row</th>
            <td>I am not a header in the 2nd row</td>
            <td>I am a 3rd column in the 2nd row</td>
        </tr>
    </table>

------

There is more you can do with tables, but not everyone is going to need [all of that functionality](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table), so I’ll leave that bit of exploration up to you.
