# Aprendendo a usar a biblioteca turtle e comentando o código

import turtle 

tela = turtle.Screen() # Cria a tela
tela.bgcolor("white") # Escolhe a cor da tela

caneta = turtle.Turtle() # Cria a tartaruga (caneta)
caneta.shape("turtle") # Escolhe a forma da caneta ("turtle", "arrow", "circle", "square", "triangle", "classic") e vc tbm pode criar formas personalizadas
caneta.color("black") # Escolhe a cor da caneta
caneta.shapesize(0.5) # Escolhe o tamanho da caneta
caneta.pensize(1) # Escolhe a espessura da linha
caneta.speed(1) # Escolhe a velocidade da caneta (1-10)

#------------------------------------------------------

caneta.fillcolor("blue") # Escolhe a cor de preenchimento
caneta.begin_fill() # Inicia o preenchimento


for x in range(4): #Loop

    caneta.forward(100)
    caneta.left(90)

caneta.end_fill() # Finaliza o preenchimento

#------------------------------------------------------

turtle.done() # Mantém a janela aberta