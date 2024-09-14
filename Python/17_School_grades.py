print("#####--------17.School grades--------#####")
""" 
U.S. high schools typically last for four years, from freshman year to senior year. 🚌💨

First, ask the user to enter their grade as an integer.

Create a four-year high school grade system using an if/elif/else statement:

grade is 9, print 'Freshman'
grade is 10, print 'Sophomore'
grade is 11, print 'Junior'
grade is 12, print 'Senior'
Everything else is 'TBD'

"""
##Variable
grade = int(input('Whats your grade form 0 - 12: '))

if grade == 9:
    print("Freshman")
elif grade == 10:
    print("Sophomore")
elif grade == 11:
    print ("Junior")
elif grade == 12:
    print ("Senior")
else:
    print("TBD")

#funcion

def calificaciones():
    nota = int(input('Ingrese su nota:  '))
    
    if nota == 9:
        return("Freshman")
    elif nota == 10:
        return("Sophomore")
    elif nota == 11:
        return ("Junior")
    elif nota == 12:
        return ("Senior")
    else:
        return("TBD")
respuesta = calificaciones()

print(respuesta)
