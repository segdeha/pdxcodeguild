__test__ = {
    'Animal': """

    >>> no_args_animal = Animal()
    >>> no_args_animal.is_animal
    True
    >>> no_args_animal.is_vegetable
    False
    >>> no_args_animal.is_mineral
    False
    >>> no_args_animal.number_of_legs
    0
    >>> no_args_animal.what_i_say is None
    True
    >>> no_args_animal.speak()
    Sorry, I don’t speak!

    >>> animal_with_args = Animal(number_of_legs=3, what_i_say='shazbat')
    >>> animal_with_args.is_animal
    True
    >>> animal_with_args.is_vegetable
    False
    >>> animal_with_args.is_mineral
    False
    >>> animal_with_args.number_of_legs
    3
    >>> animal_with_args.what_i_say is None
    False
    >>> animal_with_args.speak()
    shazbat

    """,
    'Dog': """

    >>> no_args_dog = Dog()
    >>> no_args_dog.is_animal
    True
    >>> no_args_dog.number_of_legs
    4
    >>> no_args_dog.speak()
    ruff
    >>> no_args_dog.kind
    'canine'
    >>> no_args_dog.wag()
    /wags tail

    """,
    'Pet': """

    >>> no_args_pet = Pet()
    >>> no_args_pet.name is None
    True

    >>> pet_with_arg = Pet(name='Puddles')
    >>> pet_with_arg.name is None
    False

    """,
    'PetDog': """

    >>> no_args_pet_dog = PetDog()
    >>> no_args_pet_dog.is_animal
    True
    >>> no_args_pet_dog.number_of_legs
    4
    >>> no_args_pet_dog.speak()
    ruff
    >>> no_args_pet_dog.kind
    'canine'
    >>> no_args_pet_dog.wag()
    /wags tail
    >>> no_args_pet_dog.name is None
    True

    >>> pet_dog_with_arg = PetDog(name='Fido')
    >>> pet_dog_with_arg.is_animal
    True
    >>> pet_dog_with_arg.number_of_legs
    4
    >>> pet_dog_with_arg.speak()
    ruff
    >>> pet_dog_with_arg.kind
    'canine'
    >>> pet_dog_with_arg.wag()
    /wags tail
    >>> pet_dog_with_arg.name is None
    False

    """
}


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


class Dog(Animal):
    """Blueprint for a dog (inherits from Animal)"""

    kind = 'canine'

    def __init__(self):
        super().__init__(4, 'ruff')

    def wag(self):
        print('/wags tail')


class Pet:
    """Blueprint for a generic pet"""

    def __init__(self, name=None):
        self.name = name


# class PetDog(Dog, Pet):
class PetDog(Pet, Dog):
    """Blueprint for a dog that is also a pet"""

    def __init__(self, name=None):
        super().__init__()
        self.name = name

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option
