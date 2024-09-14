import turtle

def draw_rectangle(color, width, height):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_colombia_flag():
    turtle.speed(3)

    # Flag dimensions
    flag_width = 600
    flag_height = 400

    # Position the turtle at the top-left corner of the flag
    turtle.penup()
    turtle.goto(-flag_width // 2, flag_height // 2)
    turtle.pendown()

    # Draw the yellow part (half of the flag)
    draw_rectangle("yellow", flag_width, flag_height // 2)

    # Move to the blue part position
    turtle.penup()
    turtle.goto(-flag_width // 2, 0)
    turtle.pendown()

    # Draw the blue part (quarter of the flag)
    draw_rectangle("blue", flag_width, flag_height // 4)

    # Move to the red part position
    turtle.penup()
    turtle.goto(-flag_width // 2, -flag_height // 4)
    turtle.pendown()

    # Draw the red part (quarter of the flag)
    draw_rectangle("red", flag_width, flag_height // 4)

    # Hide the turtle and display the window
    turtle.hideturtle()
    turtle.done()

# Call the function to draw the flag
draw_colombia_flag()
