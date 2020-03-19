import turtle

turtle.bgcolor('black')
turtle.pensize(2)

def line(length, angle, sides):
    for x in range(sides):
        turtle.left(angle)
        turtle.forward(length)
turtle.speed(2)
turtle.color("white", "black")

a=input('Enter the name of the equilateral polygon you want the program to draw (triangle, square, pentagon, hexagon, heptagon, octagon): ')

if a=='triangle':
    line(60, 120, 3)
elif a=='square':
    line(45, 90, 4)
elif a=='pentagon':
    line(36, 72, 5)
elif a=='hexagon':
    line(30, 60, 6)
elif a=='heptagon':
    line(25.71428571428571428571, 51.42857142857142857142, 7)
elif a=='octagon':
    line(22.5, 45, 8)
else:
    s=input('How many sides does this shape have? ')
    t=int(s)
    x=(180/t)
    y=(360/t)
    line(x, y, t)

turtle.hideturtle()
turtle.exitonclick()
