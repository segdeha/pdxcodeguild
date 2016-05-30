from car import Car


def main():
    car_1 = Car()
    car_2 = Car('Black', 4)
    car_3 = Car(number_of_doors=2, color='Blue')

    print()
    car_number = 1
    for car in [car_1, car_2, car_3]:
        print('car_' + str(car_number))
        print('number of wheels:', car.number_of_wheels)
        print('number of doors:', car.number_of_doors)
        print('color:', car.color)
        print('result of honk():')
        car.honk()
        print()
        car_number += 1

if __name__ == '__main__':
    from doctest import testmod

    testmod()
    main()
