# Write code below 💖
# 09. Pythagorean Theorem

# User Input

username = input('Enter your name: ')

print(username)

# int()
# By default, the user input is stored as a text string, which is okay for now.
# But what about when we want to get a number from a user?
# In that case, we would need to wrap an int() around the input() to convert the text string into a number:

age = int(input('what is your age?: '))
print(age)

# If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle.
# It was named after the Greek philosopher Pythagoras, born around 570 BC.

# 09. Pythagorean Theo

side_a = int(input('What is the length of a short side?: '))
side_b = int(input('What is the length of another short side?: '))

hypotenuse = ((side_a * side_a) + (side_b ** 2)) ** 0.5

print(hypotenuse)



