import turtle

turtle.speed(10)
turtle.penup()


#Funcion para dibujar los ejes X y Y coordinates

def dibujar_plano():
    longitud_eje = 300

    #Eje X    (hortizontal)
    turtle.goto(-longitud_eje,0)
    turtle.pendown()
    turtle.goto(longitud_eje,0)
    turtle.penup()

    #eje Y (vertical)
    turtle.goto(0,-longitud_eje)
    turtle.pendown()
    turtle.goto(0, longitud_eje)
    turtle.penup()

    # Función para dibujar un cuadrado alrededor del plano cartesiano
def dibujar_cuadrado():
    # Tamaño del cuadrado
    longitud_cuadrado = 600
    
    # Posición inicial en la esquina superior izquierda del cuadrado
    turtle.goto(-longitud_cuadrado/2, longitud_cuadrado/2)
    turtle.pendown()
    
    # Dibuja el cuadrado
    for _ in range(4):
        turtle.forward(longitud_cuadrado)
        turtle.right(90)
    turtle.penup()

#funcion para dibujar lineas
def dibujar_lineas(punto_inicial, punto_final, color):  
    turtle.goto(punto_inicial)
    turtle.pendown()
    turtle.pencolor(color)#colorear las lienas)
    turtle.goto(punto_final)
    turtle.penup()

dibujar_plano() #llamamos el plano!
dibujar_cuadrado()

#dibujar_lineas((0,300), (15,0),'blue')#no!!!
#This is Python!

y = 300
x = 0
while y >= 15 and x <= 300:
    dibujar_lineas((0,y),(x,0),"Green")
    y -=15
    x +=15

y = 300
x = 0
while y >= 15 and x >= -300:
    dibujar_lineas((0, y), (x, 0), 'blue')
    y -= 15
    x -= 15

y = -300
x = 0
while y <= -15 and x >= -300:
    dibujar_lineas((0, y), (x, 0), 'green')
    y += 15
    x -= 15

y = -300
x = 0
while y <= -15 and x <= 300:
    dibujar_lineas((0, y), (x, 0), 'blue')
    y += 15
    x += 15

turtle.done()




