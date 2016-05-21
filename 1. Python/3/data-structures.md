# Data Structures

There are several ways to store structured data in a Python program. (For way more detail than I go into here, read up on [Data Structures](https://docs.python.org/3/tutorial/datastructures.html) in the official Python docs.)

## List

Lists are known as “arrays” in most other languages. A list is a simple container for other values.

Example:

    supercar_makes = ['McLaren', 'Bugatti', 'Koenigsegg', 'Lamborghini', 'Ferrari', 'Aston Martin']
    
    mixed_data = ['a string', 42, {'a':'dictionary'}]

To access a member of a list, you reference its index. This makes it convenient to loop over the values. _Note that these indexes start at 0, not 1!_

Example:

    supercar_makes[2] #> 'Maserati'
    
    for i in range(0, len(supercar_makes)):
        print(supercar_makes[i])

Despite their simplicity and because they guarantee order, lists have many uses including acting as [queues](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) and [stacks](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)).

## Tuple

Tuples are immutable lists. The syntax to create them is similar (you use parentheses instead of square brackets) as is the syntax to access members.

Example:

    my_siblings = ('Mike', 'Sue', 'Kim')
    my_siblings[2] #> 'Kim'

## Dict

Called “associative arrays” in some other languages, dictionaries in Python allow you to store arbitrary data, indexed by keys. These are super efficient at retrieving values.

Example:

    food_ratings = {'burrito':9.5, 'pizza':7.0, 'curry':8.0, 'liverwurst':-472.9}
    
    character = {'name':'Brienne of Tarth', 'role': 'knight', 'kings_killed': 1, 'allegiances': ['House Tarth', 'House Baratheon', 'Renly Baratheon’s Kingsguard', 'House Tully', 'House Stark']}

You can access members (values) of the dictionary directly using ‘sub’ syntax.

Example:

    food_ratings['curry']  # > 8.0

If you want to iterate over the values in a dictionary, you must first retrieve the keys using the built-in `.keys()` method.

Example:

    for key in character.keys():
        print(character[key])

Note that the results are not guaranteed to be in any particular order!

## Set

A set is an unordered collection of data with no duplicate elements.

Example:

    fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(fruits) #> {'pear', 'banana', 'orange', 'apple'}
    
    letters_in_mississippi = set('mississippi')
    print(letters_in_mississippi) #> {'m', 'p', 's', 'i'}
    
    letters_in_missouri = set('missouri')
    print(letters_in_missouri) #> {'r', 'i', 'u', 'o', 'm', 's'}
    
    # sets enable set operations such as intersection, union, etc.
    print(letters_in_mississippi - letters_in_missouri) #> {'p'}
    print(letters_in_mississippi | letters_in_missouri) #> {'r', 'i', 'u', 'o', 'm', 'p', 's'}
    print(letters_in_mississippi & letters_in_missouri) #> {'m', 's', 'i'}
    print(letters_in_mississippi ^ letters_in_missouri) #> {'r', 'u', 'o', 'p'}

Accessing members of a set is a bit clunky. First, you need to cast the set as a list.

Example:

    list_of_letters_in_mississippi = list(letters_in_mississippi)
    print(list_of_letters_in_mississippi) #> ['m', 'p', 's', 'i']

## When should you use which type?

The following table shows some of the relative characteristics of the different types:

    | Type  | Length? | Ordered? | Lookup? | Mutable? |
    |-------|---------|----------|---------|----------|
    | List  | Yes     | Yes      | No      | Yes      |
    | Tuple | Yes     | Yes      | No      | No       |
    | Dict  | Yes     | No       | Yes     | Yes      |
    | Set   | No      | No       | No      | Yes      |

There is _no shame_ in converting between data structures within a single problem.
There is no perfect data structure that answers all of your questions, so…

## Think list when…

* You need guaranteed order
* Implementing a queue or stack
* You want to be able to count items
* “I have no idea!” — lists are a good default

## Think tuple when…

* A list would do, but you need to ensure the values don’t change once it’s created

## Think dict when…

* You want simple (fast!) lookups
* You’re mapping keys to values

## Think set when…

* You want to quickly determine whether your data contains a particular value
* You need to determine whether two sets of data contain common members
* You need to guarantee uniqueness
