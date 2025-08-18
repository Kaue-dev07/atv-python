#03 - msm código mas com algumas funcionalidades e mensagens diferentes 

import random

print("Olá!!! Vamos jogar um jogo? Selecione sua nível e acerte o número de 1 a 50:")

print("--------------")

nivel = input("Fácil(f), Médio(m) ou Difícil(d): ").lower()

chances = 0 

if nivel == "f" or nivel == "fácil":

    print("Você entrou no nível fácil, e possui 15 chances")

    chances = 15

    pontos = 11

elif nivel == "m" or nivel == "médio":

    print("Entrou no modo médio, possui 10 chances!")

    chances = 10

    pontos = 18

else:

    print("Modo difícil selecionado, se prepare com 7 chances!!!")

    chances = 7

    pontos = 25

numero = random.randint(1, 50)

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

    if chance_atual == chances // 2:

        print("------------------------------------")

        print(f"Já está na metade! Continue tentando!!!!")

    if chance_atual == chances - 1:

        print("------------------------------------")

        print(f"Você está na ultima tentativa, iras morrer gafanhoto!!!!!!")

else:

    print("------------------------------------")

    print(f"Você ultrapassou o limite de chances e morreu, o número era: {numero}!")