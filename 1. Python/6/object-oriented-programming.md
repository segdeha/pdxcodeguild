# Object-Oriented Programming

Object-Oriented Programming (OOP) is a paradigm that allows for [encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) of properties and methods into objects. This allows for well-defined [separations of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) which can make it easier to understand a complicated program and allow teams to more easily collaborate.

Classes are the basis of OOP. Think of classes as **blueprints for objects.** All objects created based on a particular class will have the same properties (also known as attributes) and methods (functions specific to the class).

------

The syntax for creating a class in Python is pretty straightforward.

Example:

    class Animal:
        """Blueprint for a generic animal"""

        # Shared properties go here
        # Common methods go here

------

Classes are required to have an `__init__` method. This is sometimes called the “constructor” method. It runs whenever an instance is created and is used to set up the initial state of the object.

Example:

    class Animal:
        """Blueprint for a generic animal"""

        # Shared properties go here

        def __init__(self):
            # Set up initial state here

        # Common methods go here

------

Let’s fill out our `Animal` class with some properties and methods.

Example:

    class Animal:
        """Blueprint for a generic animal"""

        is_animal = True
        is_vegetable = False
        is_mineral = False

        def __init__(self, number_of_legs=0, what_i_say=None):
            self.number_of_legs = number_of_legs

        def speak(self):
            if self.what_i_say is None:
                print('Sorry, I don’t speak!')
            else:
                print(self.what_i_say)

------

To use the class, you create what are called “instances” of objects based on the class.

Example:

    my_animal = Animal()

Our `Animal` class defines default values when the instance is created. So, inspecting `my_animal`, will go like the following:

    my_animal.number_of_legs  #> 0
    my_animal.is_animal  #> True
    my_animal.speak()  #> 'Sorry, I don’t speak!'

We can create another instance with different properties like this:

    my_other_animal = Animal(4, 'ruff')

    my_other_animal.number_of_legs  #> 4
    my_animal.is_animal  #> True
    my_animal.speak()  #> 'ruff'
