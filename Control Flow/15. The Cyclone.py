# Write code below 💖

height = float(input('type here your height: '))
credits = int(input('type here how many credits do you have: '))

if height >= 1.37 and credits >= 10:
  print('Enjoy the ride!')
elif height < 1.37 and credits >= 10:
  print('You are not tall enough to ride.')
elif height >= 1.37 and credits < 10:
  print('You do not have enough credits.')
else:
  print('have not met either requirement.')  
