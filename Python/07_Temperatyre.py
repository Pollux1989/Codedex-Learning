print("#####--------07. Temperature --------#####")

"""sumary_line
Create a temperature.py program that converts a temperature from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

Use the following formula and write it out in Python:


Celsius= 
(Fahrenheit32) / 1.8
 

Print out the converted temperature. 🌡️

"""

##Variable
temp_f = float(input("Temperature in F: "))
temp_c =  (temp_f - 32) / 1.8

print(temp_c)

#Funcion
def convert(f):
    return (f - 32) /1.18

print(convert(10))
