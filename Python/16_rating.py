print("#####--------16.Rating restaurant--------#####")
""" 
But what does each of the stars mean?

Start by creating a rating variable and set it equal to a decimal number.

Make a rating system using an if/elif/else statement:

rating greater than 4.5, print 'Extraordinary'
rating greater than 4, print 'Excellent'
rating greater than 3, print 'Good'
rating greater than 2, print 'Fair'
Everything else, print 'Poor'
Hint
For a refresher, to create a conditional statement:
"""

#Variables
rating = float(input('Whats the rate of this restaurant from 0  to 5: '))
if rating >= 4.5:
  print('Extraordinary ⭐️⭐️⭐️⭐️⭐️')
elif rating >= 4:
  print('Excellent ⭐️⭐️⭐️⭐️')
elif rating >= 3:
  print('Good ⭐️⭐️⭐️')
elif rating >= 2:
  print('Fair ⭐️⭐️')
else:
  print('Poor ⭐️')
########################################################################################

#Funciones
def quality():
  rating = float(input('Whats the rate of this restaurant from 0  to 5: '))
  if rating >= 4.5:
    return('Extraordinary ⭐️⭐️⭐️⭐️⭐️')
  elif rating >= 4:
    return('Excellent ⭐️⭐️⭐️⭐️')
  elif rating >= 3:
    return('Good ⭐️⭐️⭐️')
  elif rating >= 2:
    return('Fair ⭐️⭐️')
  else:
    return('Poor ⭐️')
respuesta = quality()
print(respuesta)


