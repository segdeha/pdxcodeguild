# setup

# input
name = input('Your name: ')
age = input('Your age (in years): ')

# transformation
age_plus_1 = int(age) + 1

# output
print('Hello, {name}. One year from now, you will be {age_plus_1} years old.'.format(
    name=name,
    age_plus_1=age_plus_1
))
