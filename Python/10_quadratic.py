print("#####--------10. Quadratic --------#####")

#Usando Variable
a = float(input("Type here 'a' value: "))
b = float(input("Type here 'b' value: "))
c = float(input("Type here 'c' value: "))

root_x1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root_x2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)

print(root_x1, root_x2)


#usando Funcion

def quadratic_positive (a, b, c):
    return (-b + (b*b - 4*a*c)**0.5) / (2*a)
print(quadratic_positive(5,-20,15))

def quadratic_negative (a, b, c):
    return (-b - (b*b - 4*a*c)**0.5) / (2*a)
print(quadratic_negative(5,-20,15))



