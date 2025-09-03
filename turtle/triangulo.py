import turtle

tela = turtle.Screen()
tela.bgcolor("white")

c = turtle.Turtle()
c.shape("turtle")
c.color("black")
c.shapesize(0.5)
c.pensize(1)
c.speed(1)

c.fillcolor("red")
c.begin_fill()

for x in range(3):

    c.forward(100)
    c.left(120)

c.end_fill()

turtle.done()