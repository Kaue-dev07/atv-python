import turtle

tela = turtle.Screen()
tela.bgcolor("white")

c = turtle.Turtle()
c.shape("turtle")
c.shapesize(0.5)
c.color("black")
c.speed(1)
c.pensize(1)

c.fillcolor("green")
c.begin_fill()

for x in range(2):

    c.forward(120)
    c.left(90)
    c.forward(60)
    c.left(90)

c.end_fill()

turtle.done()