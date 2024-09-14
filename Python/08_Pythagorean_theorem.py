print("#####--------09. Pythagorean Theorem --------#####")

"""
If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

Pythagorean equation looks like:

The a is the length of a short side.
The b is the length of another short side.
The c is the length of the hypotenuse.
The hypotenuse is the longest side of the right triangle.

Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

Bonus: If you are looking for a harder challenge, try the Quadratic formula!

"""

#Variable
short_side = float(input('Short Side of  triangle: '))
long_side = float(input('Long Side of triangle: '))
hypotenuse = (short_side ** 2 + long_side ** 2) ** 0.5

print(hypotenuse)


#Funciones
def calcular_hipotenusa():
    """
    Calcula la hipotenusa de un triángulo rectángulo tomando los catetos
    como entrada del usuario.
    
    Returns:
    float: Longitud de la hipotenusa.
    """
    short_side = float(input('Lado corto del triángulo: '))
    long_side = float(input('Lado largo del triángulo: '))
    hypotenuse = (short_side ** 2 + long_side ** 2) ** 0.5
    print(f"La hipotenusa es: {hypotenuse}")

# Ejemplo de uso:
calcular_hipotenusa()
