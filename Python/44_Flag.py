import turtle
# Configurar la ventana
# Window configuration
screen = turtle.Screen()
screen.title("Colombian Flag!")

# Configurar de Turtle
# Turtle configuration
t = turtle.Turtle()
t.speed(4)

# Dimensiones de la bandera
# Flag dimensions
flag_width = 300 #Ancho
flag_height = 200 #Alto

# Colores de la bandera
# Flag Colors
colors = ["#FFD700", "#0033A0", "#CE1126"] # 0 , 1 , 2 

# Dibujar la franja amarilla (mitad superior)
# Draw the yellow stripe (top half)
t.penup()
t.goto(-flag_width / 2, flag_height / 2)
t.pendown()
t.color(colors[0])#yellow!
t.begin_fill()
for _ in range(2):
    t.forward(flag_width)
    t.right(90)
    t.forward(flag_height / 2)
    t.right(90)
t.end_fill()

# Dibujar la franja azul (un cuarto inferior)
# Draw the blue stripe (lower quarter)
t.penup()
t.goto(-flag_width / 2, 0)
t.pendown()
t.color(colors[1])#Blue!
t.begin_fill()
for _ in range (2):
    t.forward(flag_width)
    t.right(90)
    t.forward(flag_height / 4)
    t.right(90)
t.end_fill()

# Dibujar la franja roja (un cuarto inferior)
# Draw the red stripe (lower quarter)
t.penup()
t.goto(-flag_width / 2, -flag_height / 4)
t.pendown()
t.color(colors[2])#
t.begin_fill()
for _ in range(2):
    t.forward(flag_width)
    t.right(90)
    t.forward(flag_height / 4)
    t.right(90)
t.end_fill()

# Ocultar turtle y mostrar la ventana
# Hide turtle and show the window
t.hideturtle
turtle.done()












            






