# Write code below 💖

import random

question = input ('Type here your question: ')

random_number = random.randint (1, 9)

if random_number == 1:
  print('Yes - definitely.')
elif random_number == 2:
  print('It is decidedly so.')
elif random_number == 3:
  print('Without a doubt.')
elif random_number == 4:
  print('Reply hazy, try again.')
elif random_number == 5:
  print('Ask again later.')
elif random_number == 6:
  print('My sources say no.')
elif random_number == 7:
  print('Better not tell you now.')
elif random_number == 8:
  print('Ask Google.')
else:
  print('Very doubtful.')

## another way:

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Magic 8 Ball:  ' + answer)

