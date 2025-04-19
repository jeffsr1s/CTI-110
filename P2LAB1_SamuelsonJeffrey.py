#Jeffrey Samuelson
#4/11/2025
#P2LAB1
#Using math expressions
import math

#Get radius from the user
radius = float(input('Enter the radius of the circle: '))

#Calculate circumference, diameter, and area
circ = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius ** 2)

#Display the results
print(f'The diameter of the circle is {diam:.1f}')
print(f'The circumference of the circle is {circ:.2f}')
print(f'The area of the circle is {area:.3f}')
