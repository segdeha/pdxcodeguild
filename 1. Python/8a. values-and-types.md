# Values and Types

Programming is about transforming data, so we need some way of representing data. A **value** is an abstract individual piece of data or fact or idea. It has no meaning on it's own. Values are the concrete nouns of programming.

**Literals** are when you literally write some values in code:

    5
    -100
    'fox'
    'David'
    3.14
    0.05

Every value is of a single **type.** A type is a kind of value or a way to interpret them.

Three basic types are:

* **Integers** are whole numbers
* **Strings** are ordered sequences of characters
* Floating point numbers or **Floats** are decimal numbers

You can sometimes represent similar ideas in multiple types:

    42
    42.0
    '42'

These are all distinct values with distinct types and thus distinct interpretations.

Sometimes the interpretation of the type allows useful, but unexpected values. A string can have no characters in it, called the **empty string**:

    ''
