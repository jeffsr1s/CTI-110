#Jeffrey Samuelson
#4/11/2025
#P2LAB2
#Using dictionaries

#Create dictionary
cars = {'Camaro':18.21,'Prius':52.36,'Model S':110,'Silverado':26, 'R1S':73}

#Get the keys to the cars
car_keys = cars.keys()

#Display the dictionary keys
print(car_keys)
print(*car_keys, sep = ', ')

#Get a car model from the user
car_name = input('Enter a car model from the list given, this is case sensitive: ')

#Get mpg for the given car
car_mpg = cars[car_name]

#Show user the name of the car with its mpg
print(f'The {car_name} gets {car_mpg} miles per gallon.')

#Get miles from user
miles_driven = float(input(f'How many miles will you drive the {car_name}?'))

#Calculate
gallons_needed = miles_driven/car_mpg

#Display results
print(f'{gallons_needed:.2f} gallons of gas or equivalent are needed to drive the {car_name} {miles_driven:.0f} miles.')
