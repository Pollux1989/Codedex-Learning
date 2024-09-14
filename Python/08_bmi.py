print("#####--------08. BMI --------#####")

"""

The body mass index (BMI) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to estimate human body fat in certain populations.

It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.


bmi= mass / heigh>2
​
 

Create a bmi.py program that calculates your own BMI.

Author's note: Psst. BMI is an archaic and oversimplified way to measure personal health. It was created by a mathematician — not a doctor! 💡
"""
#usando Funciones
mass = float(input('Type here your mass: '))
height = float(input('Type here your height: '))

bmi = mass / height * height

print ('Your Bmi is: ' + str(bmi))

#Usando Variable
def bmi(m,h):
    return m / h*h
print(bmi(80,190))

