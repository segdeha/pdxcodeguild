# setup
feet_per_mile = 5280

# input
miles = input('Number of miles: ')

# transformation
feet = int(miles) * feet_per_mile

# output
print('{feet} feet'.format(feet=feet))
