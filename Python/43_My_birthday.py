
############### 43.My Birthday! #############################

import datetime, 43bdaymessages
from 43bdaymessages import random_message

today = datetime.date.today()
next_birthday = datetime.date(2024, 6, 6)
born_date = datetime.date(1989, 6, 6)

since_my_birth =  today - born_date 
days_away =  next_birthday - today 

if today == next_birthday:
    print (random_message)
else:
    print(f'My next birthday 🎂🎁🥳 is in {days_away} away, and it\'s been {since_my_birth} days since I was born👶🍼🐣')



    