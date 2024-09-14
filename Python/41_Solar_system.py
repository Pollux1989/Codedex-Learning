print("#####--------41. solar_system--------#####")

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)
radius = 0

if random_planet == "Mercury":
    radius = 2440
elif random_planet == "Venus":
    radius = 6052
elif random_planet == "Earth":
    radius = 6371
elif random_planet == "Mars":
    radius = 3390
elif random_planet == "Saturn":
    radius = 58232
else:
    print('Ups! An Error occurred')

planet_area = round(4 * pi *radius ** 2)

print(f'The Area of {random_planet} is: {planet_area} sq mi')


