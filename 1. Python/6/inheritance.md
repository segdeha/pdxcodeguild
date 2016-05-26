# Inheritance

Inheritance is one of the more powerful concepts in [OOP](https://github.com/segdeha/pdxcodeguild/blob/master/1.%20Python/6/object-oriented-programming.md). It allows us to create a class that picks up the characteristics of another and extends or overrides them in some way.

As an example, take our `Animal` example from earlier.

    class Animal:
        """Blueprint for a generic animal"""
    
        is_animal = True
        is_vegetable = False
        is_mineral = False
    
        def __init__(self, number_of_legs=0, what_i_say=None):
            self.number_of_legs = number_of_legs
            self.what_i_say = what_i_say
    
        def speak(self):
            if self.what_i_say is None:
                print('Sorry, I don’t speak!')
            else:
                print(self.what_i_say)

Using that as our base class, we can then make classes for specific types of animals.

Example:

    class Dog(Animal):
        """Blueprint for a dog (inherits from Animal)"""
    
        kind = 'canine'
    
        def __init__(self):
            super().__init__()
            self.number_of_legs=4
            self.what_i_say='ruff'
    
        def wag(self):
            print('/wags tail')

We can even create classes that inherit from multiple other classes.

Example:

    class Pet:
        """Blueprint for a generic pet"""
    
        def __init__(self, name=None):
            self.name = name
    
    class PetDog(Dog, Pet):
        """Blueprint for a dog that is also a pet"""
    
        def __init__(self, name=None):
            super().__init__()
            self.name = name

    my_pet_dog = PetDog(name='Butch')
    
    my_pet_dog.number_of_legs  #> 4 (from Animal)
    my_pet_dog.speak()  #> 'ruff' (from Animal)
    my_pet_dog.kind  #> 'canine' (shared among all instances of Dog)
    my_pet_dog.wag()  #> '/wags tail' (from Dog)
    my_pet_dog.name  #> 'Butch' (from Pet)
