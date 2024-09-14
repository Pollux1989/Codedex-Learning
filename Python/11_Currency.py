print("#####--------11. Currency converter --------#####")

"""""

We just got home from a trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.


Make sure to Google the current exchange rates!
"""


"""
aud = float (input("How many AUD pesos do you have?: "))
eur = float (input("How many Euros do you have?: "))
usd = float (input("How many USD do you have?: "))

aud_eur = (aud*0.60)
aud_usd = (aud*0.67)

eur_aud = (eur*1.64)
eur_usd = (eur*1.10)

usd_eur = (usd*0.90)
usd_aud = (usd*1.49)

print ("Your AUD equals: " + str(aud_eur) + ' EUR')
print ("Your AUD equals: " + str(aud_usd) + ' USD')

print ("Your EUR equals: " + str(eur_aud) + ' AUD')
print ("Your EUR equals: " + str(eur_usd) + ' USD')

print ("Your USD equals: " + str(usd_eur) + ' EUR')
print ("Your USD equals: " + str(usd_aud) + ' USD')
"""

currency = int(input('Enter the Number of currency to be exchanged 1_AUD, 2_EUR or 3_USD: '))
change = int(input('Enter the currency you wish to receive 1_AUD, 2_EUR or 3_USD: '))
amount = float (input('Enter the Amount to be exchanged: '))


aud_eur = (amount*0.60)
aud_usd = (amount*0.67)

eur_aud = (amount*1.64)
eur_usd = (amount*1.10)

usd_eur = (amount*0.90)
usd_aud = (amount*1.49)

if currency == 1 and change == 2:
    print(aud_eur)
elif currency == 1 and change == 3:
    print(aud_usd)
elif currency == 2 and change == 1:
    print(eur_aud)
elif currency == 2 and change == 3:
    print(eur_aud)
elif currency == 3 and change == 1:
    print(usd_aud)
elif currency == 3 and change == 2:
    print(usd_eur)    
else:
    print('You may be choosing the same currency')












