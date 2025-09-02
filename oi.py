# Aprendendo a usar a biblioteca turtle e comentando o código

import turtle 

tela = turtle.Screen() # Cria a tela
tela.bgcolor("white") # Escolhe a cor da tela

caneta = turtle.Turtle() # Cria a tartaruga (caneta)
caneta.shape("circle") # Escolhe a forma da caneta ("turtle", "arrow", "circle", "square", "triangle", "classic") e vc tbm pode criar formas personalizadas
caneta.color("black") # Escolhe a cor da caneta
caneta.shapesize(0.5) # Escolhe o tamanho da caneta
caneta.pensize(1) # Escolhe a espessura da linha
caneta.speed(1) # Escolhe a velocidade da caneta (1-10)
