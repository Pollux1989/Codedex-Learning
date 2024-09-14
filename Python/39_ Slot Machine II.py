print("#####--------39. Slot Machine II--------#####")

import random
symbols = ['🍒','🍇','🍉','7️⃣']

def play():
  for i in range(1, 6):    
    results = random.choices(symbols, k=3)
    print(f'{results[0]} | {results[1]} | {results[2]}')
    Jackpot = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'
    Double = results[0] =='🍉' and results[1] =='🍉'  and results[2] == '🍉' 
    Triple = results[0] =='🍇' and results[1] =='🍇'  and results[2] == '🍇' 
    four_Times = results[0] =='🍒' and results[1] =='🍒'  and results[2] == '🍒' 
  
    if Jackpot:
      print('Jackpot!!! 💰')
      break
    elif Double:
      print('Double!!💵💵')
      break
    elif Triple:
      print('Triple!!💵💵💵')  
      break
    elif four_Times:
      print('4 times!!!!💵💵💵💵') 
      break
    else:
      results = random.choices(symbols, k=3)

answer = ''
while answer.upper() != 'N':
  play()
  answer = input('Keep playing? (Y/N) ')

print('Thanks for playing!')