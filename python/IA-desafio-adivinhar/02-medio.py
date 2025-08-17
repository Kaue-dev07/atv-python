#02 - nivel medio do jogo 

import random

print("Olá!!! Vamos jogar um jogo? Selecione sua nível:")

print("--------------")

nivel = input("Fácil(f), Médio(m) ou Difícil(d): ").lower()

chances = 0 

if nivel == "f" or nivel == "fácil":

    print("Você entrou no nível fácil, e possui 10 chances")

    chances = 10

    pontos = 11

elif nivel == "m" or nivel == "médio":

    print("Entrou no modo médio, possui 7 chances!")

    chances = 7

    pontos = 15

else:

    print("Modo difícil selecionado, se prepare com 5 chances!!!")

    chances = 5

    pontos = 20

numero = random.randint(1, 30)

for chance_atual in range(1, chances + 1):

    print("--------------------------------------")

    pontos -= 1 

    tentativa = int(input(f"Chances {chance_atual} de {chances}, tente: "))

    if tentativa > numero:

        print("------------------------------------")

        print(f"Seu número é menor!")

    elif tentativa < numero:

        print("------------------------------------")

        print(f"Seu número é maior!")

    else:

        print("------------------------------------")

        print(f"Você acertou, o número era: {numero} e ganhou {pontos}!!!")

        break

else:

    print("------------------------------------")

    print(f"Você ultrapassou o limite de chances e morreu, o número era: {numero}!")