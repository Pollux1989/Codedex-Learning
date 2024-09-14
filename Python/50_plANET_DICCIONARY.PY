solar_system = { "mercurio": {"numero": 1, "masa": 0.06, "num_lunas": 0, "diametro":{'polar': 12, 'ecuato': 13}},
                 "venus": {"numero": 2, "masa": 0.82, "num_lunas": 0, "diametro":{'polar': 12, 'ecuato': 13}},
                 "tierra": {"numero":3, "mas":0.8, "num_lunas": 1, "diametro":{'polar': 12, 'ecuato':1}},
                 "marte": {"numero":4, "mas":0.53, "num_lunas": 1, "diametro":{'polar': 13, 'ecuato':3}},      
                }


solar_system.update({'venus':{"numero": 4}})
solar_system.update({'venus':{"diametro":{'polar': 5}}})

print (f"{solar_system}")

"""Dynamic programming with dictionaries
Completed
100 XP
3 minutes
In your program, you want to perform various calculations, like totaling the number of moons. Additionally, as you get into more advanced programming, you might find that you're loading this type of information from files or a database, rather than coding directly into Python.

To help support these scenarios, Python enables you to treat both the keys and values inside of a dictionary as a list. You can dynamically determine keys and values, and perform various calculations.

Imagine a dictionary storing monthly rainfall amounts. You would likely have keys for each month and the associated rainfall. You want to add up the total rainfall, and writing the code to perform the operation by using each individual key would be rather tedious.

Retrieve all keys and values
The keys() method returns a list object that contains all the keys. You can use this method to iterate through all items in the dictionary.

Imagine you have the following dictionary, storing the last three months of rainfall.

"""

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print (f'{key}: {rainfall[key]} cm')


if 'december' in rainfall:
    rainfall ['december'] = rainfall ['december'] + 1

else:
    rainfall ['december'] = 1


for key in rainfall.keys():
    print (f'{key}: {rainfall[key]} cm') # Because december exists, the value will be 3.1

###########################################################
"""
Retrieve all values
Similar to keys(), values() returns the list of all values in a dictionary without their respective keys.
values() can be helpful when you're using the key for labeling purposes, such as the preceding example,
in which the keys are the name of the month. You can use values() to determine the total rainfall amount:
"""

total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'Total {total_rainfall} in cm in the last quarter')
