import turtle

turtle.bgcolor('black')
turtle.pensize(2)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(2)
turtle.color("red", "pink")


turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.penup()
turtle.setpos(0,100)
turtle.write('you\'re my person', move='True', align='center', font='veranda, 14')
turtle.setpos(0,60)
turtle.write('love, Liz', move='True', align='center', font='veranda, 14')
turtle.hideturtle()
turtle.exitonclick()
