# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

#----------------16. Sorting Hat----------------

#----------------Question 1---------------------

print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')

answer = int(input('Type your answer 1-2: '))

if answer == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif answer == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('wrong number')

#----------------Question 2---------------------

print('Q2) When Im dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')

answer = int(input('Type your answer 1-4: '))

if answer == 1:
  Hufflepuff += 2
elif answer == 2:
  Slytherin += 2
elif answer == 3:
  Ravenclaw += 2
elif answer == 4:
  Gryffindor += 2
else:
  print('wrong number')

#----------------Question 3---------------------

print('Q3) Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')

answer = int(input('Type your answer 1-4: '))

if answer == 1:
  Slytherin += 4
elif answer == 2:
  Hufflepuff += 4
elif answer == 3:
  Ravenclaw += 4
elif answer == 4:
  Gryffindor += 4
else:
  print('wrong number')

print('===============')
print('The Sorting Hat is Talking🪄!!!')
print('===============')

print("Gryffindor",Gryffindor)
print("Ravenclaw", Ravenclaw)
print("Hufflepuff", Hufflepuff)
print("Slytherin", Slytherin)


if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print("Ah, bravery simmering beneath the surface... or maybe not so far beneath. You possess a daring spirit, a Gryffindor I smell! Where dwell the brave at heart, their daring, nerve and chivalry set 🦁Gryffindors apart.")
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print("A mind that hums with curiosity! A thirst for knowledge that rivals any I've encountered. You value wit, learning, and a sharp mind. 🦅Ravenclaw would welcome one such as yourself!")
elif Hufflepuff >= Slytherin:
  print("Hmm, a sense of fair play and loyalty... a dedication to hard work and seeing things through. You remind me of Helga Hufflepuff herself! 🦦Hufflepuff values these things most of all.")
else:
  print("Now, here's an interesting one. Ambition, a sharp mind, and perhaps a hint of cunning. You crave power and greatness, do you not? 🐍Slytherin could use someone with your talents.")


  













