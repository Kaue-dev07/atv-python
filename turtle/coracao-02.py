import turtle

tela = turtle.Screen()
tela.bgcolor("white")

c = turtle.Turtle()
c.shape("turtle")
c.color("black")
c.shapesize(0.5)
c.pensize(1)
c.speed(1)

c.fillcolor("yellow")
c.begin_fill()

#----------------------------------------------------------------------------------

c.right(180)

c.penup()

c.forward(90)

c.pendown()

c.left(130)

for x in range(2):

    c.forward(100)

    c.left(100)

c.right(60)

for i in range(2):
    c.circle(32 , 180)

    c.right(180)

#----------------------------------------------------------------------------------

c.end_fill()

turtle.done()