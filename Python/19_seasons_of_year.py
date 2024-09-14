print("#####--------19. Seasons of the Year--------#####")

''' Ah, the four seasons in the year — winter, spring, summer, or fall; all you have to do is call!

Ask the user the month number using the input() function.

Check for the four seasons using an if/elif/else statement and logical operators:

month is 1, 2, 3, print 'Winter 🌨️'
month is 4, 5, 6, print 'Spring 🌱'
month is 7, 8, 9, print 'Summer 🌻'
month is 10, 11, 12, print 'Autumn 🍂'
Everything else is 'Invalid'
Logical operators in Python include the and and or keywords. Which one should you use?'''



#variable
month = int(input('Which month of the year is this: '))

if month == 1 or month == 2 or month == 3:
    print ('Winter')
elif month == 4 or month == 5 or month == 6:
    print ('Spring')
elif month == 7 or month == 8 or month == 9:
    print ('Summer')
elif month == 10 or month == 11 or month == 12:
    print ('Autumn')
else:
    print('invalid')

##Funion mejorada ahahah
def mes_ano():
    mes = int(input('¿En qué mes del año estamos (1-12)?: '))

    if mes in [1, 2, 3]:
        return 'Estamos en Invierno'
    elif mes in [4, 5, 6]:
        return 'Estamos en Primavera'
    elif mes in [7, 8, 9]:
        return 'Estamos en Verano'
    elif mes in [10, 11, 12]:
        return 'Estamos en Otoño'
    else:
        return '¡Ingresa un mes válido!'
# Llamada a la función y muestra del resultado
estacion = mes_ano()
print(estacion)
