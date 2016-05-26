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
        super().__init__()
        self.number_of_legs=4
        self.what_i_say='ruff'

    def wag(self):
        print('/wags tail')

class Pet:
    """Blueprint for a generic pet"""

    def __init__(self, name=None):
        self.name = name

class PetDog(Dog, Pet):
    """Blueprint for a dog that is also a pet"""

    def __init__(self, name=None):
        super().__init__()
        self.name = name
