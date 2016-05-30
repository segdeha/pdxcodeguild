
__test__ = {
    "Public API": """

    >>> my_car = Car()
    >>> my_car.number_of_wheels
    4
    >>> my_car.color
    'Black'
    >>> my_car.number_of_doors
    4
    >>> my_car.honk()
    honk

    """
}


class Car:
    """Blueprint for Car objects"""

    number_of_wheels = 4

    def __init__(self, color='Black', number_of_doors=4):
        self.color = color
        self.number_of_doors = number_of_doors

    @staticmethod
    def honk():
        print('honk')

if __name__ == '__main__':
    from doctest import testmod

    testmod()
