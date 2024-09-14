print("#####--------12. Relational Operators --------#####")
"""
A lot of the times inside conditions, we are comparing two values. To do so,
we need to use a different type of operators called relational operators that compares values:

== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to


In chemistry, pH is a scale used to specify the acidity or basicity of a liquid.

Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

First, create a ph variable and ask the user for a value between 0 and 14.

Write an if, elif, else statement that:

If ph is greater than 7, output "Basic".
If ph is less than 7, output "Acidic".
Else, output "Neutral".
"""
#Variable
ph_level = float(input("Type here the Ph level from 1 - 15: "))

if ph_level >= 10 < 15:
    print ("Ph level is Basic")
elif ph_level >= 5 < 9:
    print ("Ph level is Acidic")
else:
    print ("Ph level is Neutral")

#Funciones

def nivel_ph(ph_level):
    ph_level = float(input("Type here the Ph level from 1 - 15: "))

    if ph_level >= 10 < 15:
        return ("Ph level is Basicc")
    elif ph_level >= 5 < 9:
        return ("Ph level is Acidicc")
    else:
        return ("Ph level is Neutral")
    
respuesta = nivel_ph(ph_level)
    
print (respuesta)




