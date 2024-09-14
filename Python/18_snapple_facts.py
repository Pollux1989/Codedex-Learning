print("#####--------18.Snapple facts--------#####")
""" 
Snapple is a famous tea drink brand from Queens, New York. Each bottle cap comes with a silly fun fact.

Use the random module to create a number from 0 to 5.

Then use an if/elif/else statement to print out one of these six random Snapple facts:

0 - 'Flamingos turn pink from eating shrimp.'
1 - 'The only food that doesn't spoil is honey.'
2 - 'Shrimp can only swim backwards.'
3 - 'A taste bud's life span is about 10 days.'
4 - 'It is impossible to sneeze while sleeping.'
5 - 'It is illegal to sing off-key in North Carolina.'

"""
'''

import random

snapple_facts = random.randint(0,5)

if snapple_facts ==0:
    print("Flamingos turn pink from eating shrimp")
elif snapple_facts ==1:
    print("The only food that doesn't spoil is honey.")
elif snapple_facts ==2:
    print('Shrimp can only swim backwards')
elif snapple_facts ==3:
    print('A taste buds life span is about 10 days')
elif snapple_facts ==4:
    print ('It is impossible to sneeze while sleeping')
elif snapple_facts ==5:
    print('It is illegal to sing off-key in North Carolina.')
else:
    print('bye')
'''
import random

def random_fact():
    """
    Muestra un hecho curioso aleatorio basado en un número generado al azar.
    """
    snapple_facts = random.randint(0, 5)
    
    if snapple_facts == 0:
        print("Flamingos turn pink from eating shrimp")
    elif snapple_facts == 1:
        print("The only food that doesn't spoil is honey.")
    elif snapple_facts == 2:
        print("Shrimp can only swim backwards")
    elif snapple_facts == 3:
        print("A taste buds life span is about 10 days")
    elif snapple_facts == 4:
        print("It is impossible to sneeze while sleeping")
    elif snapple_facts == 5:
        print("It is illegal to sing off-key in North Carolina.")
    else:
        print("bye")

# Ejemplo de uso
random_fact()

