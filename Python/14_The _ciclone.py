print("#####--------14.Ciclone-------#####")
'''
Since 1927, "The Cyclone" rollercoaster has delighted riders visiting Coney Island in Brooklyn, New York. 🎢

They're now installing a new entry system (the height requirement is 137 cm and the cost is 10 credits) and need your help writing the program for it!

Create a new file called the_cyclone.py.

Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

Use a combination of relational and logical operators to create the rules:

If they are tall enough and have enough credits, print "Enjoy the ride!"
Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
Else, print a message saying they have not met either requirement.

'''
#variable
height = float(input('Enter your height in meter, ex: 1.85: '))
credits = float(input('Enter your credits: '))

if height >= 1.37 and credits >= 10:
    print('Enjoy the ride!')
elif credits >= 10 and height <= 1.37:
    print('You are not tall enough to ride.')
elif height >=1.37 and credits <= 10:
    print('You do not have enough credits')
else:
    print('you have not met either requirement.')


#funcion
def ciclone():
    altura = float(input("Ingrese su estatura en metros, ejemplo 1.85: "))
    creditos = float(input("Ingrese la cantidad de creditos: "))

    if altura >= 1.37 and creditos >= 10:
        return('Enjoy the ride!')
    elif creditos >= 10 and altura <= 1.37:
        return('You are not tall enough to ride.')
    elif altura >=1.37 and creditos <= 10:
        return('You do not have enough credits')
    else:
        return('you have not met either requirement.')
respuesta = ciclone()
print(respuesta)

