"""

>>> calculate_change(99)
'Your change for 99¢ consists of 3 quarters, 2 dimes, 4 pennies.'

"""


def calculate_change(cents):
    """Return a formatted string with only the coins listed that are needed for the change.

    >>> calculate_change(99)
    'Your change for 99¢ consists of 3 quarters, 2 dimes, 4 pennies.'

    >>> calculate_change(47)
    'Your change for 47¢ consists of 1 quarter, 2 dimes, 2 pennies.'

    >>> calculate_change(12)
    'Your change for 12¢ consists of 1 dimes, 2 pennies.'

    >>> calculate_change(0)
    'Your change for 0¢ consists of .'
    """

    # setup
    quarter_value = 25
    dime_value = 10
    nickle_value = 5

    # transformation
    num_quarters, remainder = get_coins_and_remainder_for_value(quarter_value, cents)
    num_dimes, remainder = get_coins_and_remainder_for_value(dime_value, remainder)
    num_nickles, num_pennies = get_coins_and_remainder_for_value(nickle_value, remainder)

    # output
    output = 'Your change for {cents}¢ consists of '

    pieces = []

    if num_quarters > 0:
        quarters_string = 'quarter' if num_quarters == 1 else 'quarters'
        pieces.append('{num_quarters} ' + quarters_string)
        # pieces.append('{num_quarters} quarters')

    if num_dimes > 0:
        pieces.append('{num_dimes} dimes')

    if num_nickles > 0:
        pieces.append('{num_nickles} nickles')

    if num_pennies > 0:
        pieces.append('{num_pennies} pennies')

    output += ', '.join(pieces) + '.'

    return output.format(
        cents=cents,
        num_quarters=num_quarters,
        num_dimes=num_dimes,
        num_nickles=num_nickles,
        num_pennies=num_pennies
    )


def get_coins_and_remainder_for_value(coin, value):
    """Return the number of coins for the given value

    >>> get_coins_and_remainder_for_value(25, 99)
    (3, 24)

    >>> get_coins_and_remainder_for_value(10, 99)
    (9, 9)

    >>> get_coins_and_remainder_for_value(5, 99)
    (19, 4)

    >>> get_coins_and_remainder_for_value(1, 99)
    (99, 0)
    """
    return value // coin, value % coin


def prompt_user():
    """Gather user input, calculate change, print result"""
    cents = int(input('How much change do you need (enter a number of cents under 100)? '))
    change = calculate_change(cents)
    print(change)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    prompt_user()
