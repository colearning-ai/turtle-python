import turtle
turtle.penup()
turtle.speed(0)
turtle.setpos(0,0)
turtle.pendown()
turtle.color("white", "black")
turtle.colormode(1.0)
SQUARES = 60
SIDE = 150
shade = 0.0
for count in range(SQUARES):
    turtle.fillcolor(shade, shade, shade)
    turtle.begin_fill()
    turtle.left(360 // SQUARES)
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.forward(SIDE)
    turtle.left(90)
    turtle.end_fill()
    shade += 1.0 / float(SQUARES)

turtle.done() 
