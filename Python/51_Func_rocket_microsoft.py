'''
Basics of Python functions
Completed
100 XP
3 minutes
Functions are the next step after you've learned Python's programming basics. In its simplest form,
 a function contains code that always returns a value (or values). In some cases, a function also has optional or required inputs.
When you start writing code that duplicates other parts of the program, it becomes a perfect opportunity to extract the code into a function.
Although sharing common code through functions is useful, you can also limit the size of code by extracting parts out into smaller (more readable) functions.
Programs that avoid duplication and prevent large functions by using smaller functions are more readable and maintainable.
They're also easier to debug when things aren't working right. Several rules about function inputs are critical for you to fully take advantage of everything that functions have to offer.
Important
Although we're using the term input to describe what functions take in, these elements are usually called arguments or parameters.
For consistency in this module, we'll refer to inputs as arguments.
'''

# Functions with no arguments
#To create a function, you use the def keyword followed by a name,
#Parentheses, and then the body with the function code:

def rocket_parts():
    print("payload, propellant, structure")

rocket_parts()
output = rocket_parts()
output is None

'''
Required and optional arguments
In Python, several built-in functions require arguments.
Some built-in functions make arguments optional. 
Built-in functions are immediately available, so you don't need to import them explicitly.
An example of a built-in function that requires an argument is any(). 
This function takes an iterable (for example, a list) and returns True if any item in the iterable is True. Otherwise, it returns False.

Use function arguments in Python
Completed
100 XP
3 minutes
Now that you know how to create a function with no inputs, the next step is to create functions that require an argument. Using arguments makes functions more flexible, because they can do more and conditionalize what they do.

Requiring an argument
If you're piloting a rocket ship, a function without required inputs is like a computer with a button to tell you the time. If you press the button, a computerized voice tells you the time. But a required input can be a destination to calculate travel distance. Required inputs are called arguments to the function.

To require an argument, put it within the parentheses:
'''

def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'
distance_from_earth('Moon')


'''
Multiple required arguments
To use multiple arguments, you must separate them by using a comma.
Let's create a function that can calculate how many days it takes to reach a destination, 
given distance and a constant speed:
'''

def day_to_complete ( distance, speed):
    hours = distance / speed
    return hours / 24
day_to_complete(150000, 56)

total_days = day_to_complete(150000, 56) #
print (total_days)#111.607142
round(total_days) #112
round(day_to_complete(238855, 75)) #133


''''



'''