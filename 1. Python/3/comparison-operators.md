# Comparison Operators

All types have the concept of equality. Two strings could have the same value. Two Booleans could have the same value.

Many types also have a concept of order. Integers are ordered on the number line. Strings can be in alphabetical order. But not all types. E.g., Booleans don't have an order.

Python gives us operators that let us check order and equality on types that support it. They all _return_ Booleans.

The **equals** operator is `==`:

    3 == 3 #> True
    'hi' == 'bye' #> False
    True == False #> False

The **less-than** operator is `<`:

    5 > 9  #> False
    'zebra' > 'aardvark' #> True

The **greater-than** operator is `>`:

    5 < 9  #> True
    'zebra' < 'aardvark' #> False

The **not-equals** operator is `!=`:

    3 != 3  #> False
    'hi' != 'bye' #> True
    True != False #> True

There are also **greater-than-or-equal-to** (`>=`) and **less-than-or-equal-to** (`<=`) operators.

The rule-of-thumb from basic operators still applies:
avoid mixing types. Equals and not-equals do allow you to.

    'hi' == 6 #> False
    'hi' != 6 #> True

Most of the other operators don’t.

    True > 5 #> throws TypeError
    'hi' <= 2.2 #> throws TypeError

Remember, these are operators, just like `+` or `*` or `//`! They just return Booleans. They can take in any expression and can be used as an expression.

    names_match = 'Bob' == 'Al'
    is_positive = abs(num) == num
    print(age == 32)
