print("#####--------13. magic ball--------#####")

"""  
Instructions
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:

Question:      [Question]
Magic 8 Ball:  [Answer]

for Example:
Question:      Is Codédex better than Udemy yet?
Magic 8 Ball:  Better not tell you now.
"""

#variable
import random
question = input("Whats your Question: ")
answers = random.randint(1,3)

if answers == 1:
    print ("Yes - definitely.")
elif answers == 2:
    print ("Without a doubt.")
else:
    print ("YES!!")

#Funcion
def magic_ball():
    input ("Whats your Question: ")
    answers = random.randint(1,3)
    if answers == 1:
        return ("Yes - definitely.")
    elif answers == 2:
        return ("Without a doubt.")
    else:
        return ("YES!!")
respuesta = magic_ball()
print (respuesta)


