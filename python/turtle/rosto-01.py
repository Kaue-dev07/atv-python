#fazer um mega blaster rosto feliz

import turtle

tela = turtle.Screen()
tela.bgcolor("black")

c = turtle.Turtle()
c.shape("turtle")
c.color("yellow")
c.shapesize(0.5)
c.pensize(1)
c.speed(10)

#rosto

c.fillcolor("yellow")
c.begin_fill()

c.penup()
c.right(90)
c.forward(170)
c.left(90)
c.pendown()
c.circle(200)

c.end_fill()

#--------------

c.penup()
c.left(90)
c.forward(280)
c.left(90)
c.forward(70)

#olho esquerdo

c.fillcolor("white")
c.begin_fill()

c.color("white")
c.pendown()
c.circle(40)

c.end_fill()

c.penup()
c.left(90)
c.forward(15)
c.pendown()

c.color("black")
c.fillcolor("black")
c.begin_fill()

c.right(90)
c.circle(20)

c.end_fill()

#-------------

c.penup()
c.right(90)
c.forward(15)
c.right(90)
c.forward(140)
c.left(180)
c.pendown()

#olho direito 

c.color("white")
c.fillcolor("white")
c.begin_fill()
c.circle(40)
c.end_fill()
c.left(90)
c.penup()
c.forward(15)
c.pendown()
c.right(90)
c.color("black")
c.fillcolor("black")
c.begin_fill()
c.circle(20)
c.end_fill()

#-------------

c.penup()
c.right(90)
c.forward(15)
c.left(90)
c.forward(70)
c.left(90)
c.forward(140)
c.right(90)
c.forward(80)
c.left(150)
c.pendown()

# boca

c.right(60)
c.fillcolor("red")
c.begin_fill()
c.circle(80, 180)
c.left(90)
c.forward(160)
c.end_fill()

#-------------

c.penup()
c.left(180)
c.forward(40)
c.right(90)
c.pendown()

# dentes esquerdo

c.fillcolor("white")
c.begin_fill()
c.forward(30)
c.left(45)
c.forward(10)
c.left(45)
c.forward(20)
c.left(45)
c.forward(10)
c.left(45)
c.forward(30)
c.left(90)
c.forward(75)
c.end_fill()

#-------------

c.penup()
c.left(180)
c.forward(90)
c.right(90)
c.pendown()

# dente direito

c.fillcolor("white")
c.begin_fill()
c.forward(30)
c.left(45)
c.forward(10)
c.left(45)
c.forward(20)
c.left(45)
c.forward(10)
c.left(45)
c.forward(30)
c.left(90)
c.forward(80)
c.end_fill()

#-------------

c.penup()
c.right(90)
c.forward(180)
c.left(90)
c.pendown()

#sobrancelha esquerda

c.fillcolor("black")
c.begin_fill()
c.forward(30)

for x in range(5):
    c.left(10)
    c.forward(10)

c.left(150)
c.left(10)
c.forward(10)
c.right(10)
c.forward(10)
c.right(10)
c.forward(20)
c.right(5)
c.forward(30)
c.left(70)
c.forward(10)
c.end_fill()

#-------------

c.penup()
c.right(80)
c.forward(90)

# sombrancelha direita

c.fillcolor("black")
c.begin_fill()
c.forward(30)

for x in range(5):
    c.right(10)
    c.forward(10)

c.right(150)
c.right(10)
c.forward(10)
c.left(10)
c.forward(10)
c.left(10)
c.forward(20)
c.left(5)
c.forward(30)
c.right(70)
c.forward(10)
c.end_fill()

turtle.done()
