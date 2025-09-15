import turtle

tela = turtle.Screen()
tela.bgcolor("white")

c = turtle.Turtle()
c.shape("turtle")
c.color("black")
c.shapesize(0.5)
c.pensize(1)
c.speed(5)

c.fillcolor("purple")
c.begin_fill()

#----------------------------------------------------------------------------------

c.penup()

c.forward(180)

c.pendown()

c.left(90)

c.circle(100 , 180 ) # Desenha um círculo com raio 100 e 180 graus (meia volta) 

c.right(180)

c.circle(100 , 180 ) # Desenha um círculo com raio 100 e 180 graus (meia volta) 

c.left(40)

c.forward(300)

c.left(99)

c.forward(310)

#----------------------------------------------------------------------------------

c.end_fill()

turtle.done()