
print("#####--------38. Slot Machine--------#####")

import random

symbols = ['🍒','🍇','🍉','7️⃣']

results = random.choices(symbols, k=3)


print(f'{results[0]}  |  {results[1]}  |  {results[2]}')

if (results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'):
    print('Jackpot!🤑💰💵')
elif (results[0] =='🍉' and results[1] =='🍉'  and results[2] == '🍉' ):
    print('Double!!💵💵')
elif (results[0] =='🍇' and results[1] =='🍇'  and results[2] == '🍇' ):
    print('Triple!!💵💵💵')     
elif (results[0] =='🍒' and results[1] =='🍒'  and results[2] == '🍒' ):
    print('4 times!!!!💵💵💵💵') 
else:
    print('Thanks for playing')
