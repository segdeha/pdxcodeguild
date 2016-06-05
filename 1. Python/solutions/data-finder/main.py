"""Functions to find data within a data structure.

When the file is run directly, the user experience goes like this:

- Prompt the user for which category they’re interested in
  - Prompt the user for either the top-level key to the dataset or an item from one of the lists in the dataset
    - If they choose a top-level key, prompt them for a child-key
      - If we find the child-key, print the list items for the top-level and child keys
    - If they choose an item from a list, print the top-level and child keys

When the file is imported as a module, any of the functions are available to be used.
See the docstrings in the `__test__` variable for usage details.

"""

import os
import json

__test__ = {
    'generic': """

    >>> get_items_by_parent_key_and_child_key({'foo':{'bar':['baz']}}, 'foo', 'bar')
    ['baz']

    >>> get_items_by_parent_key_and_child_key({'foo':{'bar':['baz']}}, 'abc', 'xyz') is None
    True

    >>> get_parent_key_and_child_key_by_list_item({'foo':{'bar':['baz']}}, 'baz')
    ('foo', 'bar')

    >>> get_parent_key_and_child_key_by_list_item({'foo':{'bar':['baz']}}, 'xyz')
    (None, None)

    >>> format_list_as_string(['a'])
    'a'

    >>> format_list_as_string(['a', 'b'])
    'a or b'

    >>> format_list_as_string(['a', 'b', 'c'], 'and')
    'a, b and c'

    >>> format_list_as_string('xyz')
    'x, y or z'

    >>> format_list_as_string(42)
    42

    """,

    'nfl': """

    >>> NFL = {
    ...     'AFC': {
    ...         'East': ['Buffalo Bills', 'Miami Dolphins', 'New England Patriots', 'New York Jets'],
    ...         'North': ['Baltimore Ravens', 'Cincinnati Bengals', 'Cleveland Browns', 'Pittsburgh Steelers'],
    ...         'South': ['Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Tennessee Titans'],
    ...         'West': ['Denver Broncos', 'Kansas City Chiefs', 'Oakland Raiders', 'San Diego Chargers']
    ...     },
    ...     'NFC': {
    ...         'East': ['Dallas Cowboys', 'New York Giants', 'Philadelphia Eagles', 'Washington Redskins'],
    ...         'North': ['Chicago Bears', 'Detroit Lions', 'Green Bay Packers', 'Minnesota Vikings'],
    ...         'South': ['Atlanta Falcons', 'Carolina Panthers', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
    ...         'West': ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']
    ...     }
    ... }

    >>> get_items_by_parent_key_and_child_key(NFL, 'NFC', 'West')
    ['Arizona Cardinals', 'Los Angeles Rams', 'San Francisco 49ers', 'Seattle Seahawks']

    >>> get_parent_key_and_child_key_by_list_item(NFL, 'Seattle Seahawks')
    ('NFC', 'West')

    """,

    'cuisines': """

    >>> CUISINES = {
    ...     'Thai': {
    ...         'Pad Thai': ['Noodles', 'Peanuts', 'Egg', 'Green Onions', 'Bean Sprouts']
    ...     },
    ...     'Mexican': {
    ...         'Enchiladas': ['Tortillas', 'Enchilada Sauce', 'Cheese'],
    ...         'Burritos': ['Tortillas', 'Beans', 'Rice', 'Cheese']
    ...     },
    ...     'Italian': {
    ...         'Spaghetti': ['Pasta', 'Red Sauce', 'Oregano']
    ...     },
    ...     'Indian': {
    ...         'Palak Paneer': ['Cheese', 'Spinach', 'Garlic', 'Onion', 'Tumeric', 'Cream']
    ...     }
    ... }

    >>> get_items_by_parent_key_and_child_key(CUISINES, 'Thai', 'Pad Thai')
    ['Noodles', 'Peanuts', 'Egg', 'Green Onions', 'Bean Sprouts']

    >>> get_parent_key_and_child_key_by_list_item(CUISINES, 'Bean Sprouts')
    ('Thai', 'Pad Thai')

    """,

    'movies': """

    >>> MOVIES = {
    ...     'Action Thriller': {
    ...         'Mad Max: Fury Road': ['Tom Hardy', 'Charlize Theron', 'Nicholas Hoult', 'Zoë Kravitz'],
    ...         'Twister': ['Helen Hunt', 'Bill Paxton', 'Cary Elwes', 'Philip Seymour Hoffman']
    ...     },
    ...     'Sci-Fi': {
    ...         'Star Wars: Episode VII - The Force Awakens': [
    ...             'Harrison Ford',
    ...             'Mark Hamill',
    ...             'Carrie Fisher',
    ...             'Adam Driver',
    ...             'Daisy Ridley',
    ...             'John Boyega'
    ...         ],
    ...         'Sunshine': ['Cillian Murphy', 'Michelle Yeoh', 'Troy Garity', 'Rose Byrne', 'Chris Evans']
    ...     },
    ...     'Comedy': {
    ...         'Raising Arizona': ['Nicolas Cage', 'Holly Hunter', 'John Goodman'],
    ...         'Zoolander 2': ['Ben Stiller', 'Owen Wilson', 'Penélope Cruz']
    ...     }
    ... }

    >>> get_items_by_parent_key_and_child_key(MOVIES, 'Comedy', 'Zoolander 2')
    ['Ben Stiller', 'Owen Wilson', 'Penélope Cruz']

    >>> get_parent_key_and_child_key_by_list_item(MOVIES, 'Penélope Cruz')
    ('Comedy', 'Zoolander 2')

    """
}


def get_items_by_parent_key_and_child_key(data, parent_key, child_key):
    """Return a list of items for the given parent_key and child_key or None if there is no match."""

    if parent_key in data and child_key in data[parent_key]:
        return data[parent_key][child_key]
    else:
        return None


def get_parent_key_and_child_key_by_list_item(data, list_item):
    """Return a tuple of the parent_key and child_key for the given list item or None if there is no match."""

    for parent_key in data:
        for child_key in data[parent_key]:
            try:
                # If `.index` succeeds, it returns a number between 0 and the index of the last item in the list
                # If it fails, it throws a ValueError
                if data[parent_key][child_key].index(list_item) > -1:
                    return parent_key, child_key  # Return results as a tuple
            except ValueError:
                continue

    return None, None


def format_list_as_string(list_of_strings, conjunction='or'):
    """Format a list of strings as a string where all items are separated by commas and the last 2 items are
    separated by the given conjunction (defaults to 'or')."""

    try:
        if len(list_of_strings) == 1:
            return list_of_strings[0]  # Usually [0] is a sign of brittleness, but we *just* made sure it exists
        else:  # More than 1 item in the list
            strings = list(list_of_strings)  # Copy the list so we don’t pop off the last member of the actual data
            last_item = strings.pop()
            delimiter = ' {conjunction} '.format(conjunction=conjunction)
            return delimiter.join([', '.join(strings), last_item])
    except TypeError:  # Don’t know what to do with this (e.g., an int), so just return the original value
        return list_of_strings


def main(filename):
    """Prompt for user input, get a result from the data, print a nicely formatted answer."""

    # Get the directory in which the script is executing
    # This allows me to run main.py from a directory other than the one it sits in and have it still find data.json
    dirname = os.path.split(os.path.abspath(__file__))[0]

    # Open the file, read the data, convert the JSON to a data structure, close the file
    with open('/'.join([dirname, filename]), 'r') as f:
        data = json.loads(f.read())

    data_type = input('Are you interested in {choices}? '.format(
        choices=format_list_as_string(data.keys())
    ))

    if data_type not in data:
        print('Sorry, I only know {choices}!\n'.format(
            choices=format_list_as_string(data.keys(), 'and')
        ))
        main(filename)

    # Simplify data handling by only working with the slices of the data we need
    dataset = data[data_type]['data']
    strings = data[data_type]['strings']

    parent_keys = dataset.keys()
    user_input = input(strings['first_prompt'].format(
        parent_keys=format_list_as_string(parent_keys)
    ))

    if user_input in parent_keys:  # There’s a match at the top level of our dataset
        parent_key = user_input
        child_keys = list(dataset[parent_key].keys())
        child_key = input(strings['second_prompt'].format(
            child_keys=format_list_as_string(child_keys)
        ))
        items = get_items_by_parent_key_and_child_key(dataset, parent_key, child_key)

        if items is None:
            print('Sorry, I couldn’t find a match for that.\n')
            main(filename)
        else:  # There’s a match for both the parent and child keys
            print()
            print(strings['two_inputs_output'].format(
                parent_key=parent_key,
                child_key=child_key,
                items='\n• '.join(items)
            ))
            print()
    else:  # Assume the user gave us an item from a list
        list_item = user_input
        parent_key, child_key = get_parent_key_and_child_key_by_list_item(dataset, list_item)

        if parent_key is None:  # No matching list item
            print('Sorry, I couldn’t find a match for that.\n')
            main(filename)
        else:
            print()
            print(strings['one_input_output'].format(
                list_item=list_item,
                parent_key=parent_key,
                child_key=child_key
            ))
            print()

    again = input('Do you want to try again (y/n)? ').lower()

    if again == 'y':
        main(filename)
    else:  # Exit on any other input besides 'y'
        import sys

        print('Goodbye!')
        sys.exit()


if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
    main('data.json')  # Kick off the program, passing it the location of our data file
