#04 - msm código mas com algumas funcionalidades e mensagens diferentes e sistema de jogar dnv 

import random

from datetime import datetime

hora = datetime.now().hour

if 6 <= hora < 12:

    print("Bom dia, como vai? Vamos começar o jogo!!!")

elif 12 <= hora < 18:

    print("Boa tarde! E que tarde agradavel, vamos inciar o jogo!")

else:

    print("O que faz aqui tão tarde? Vamos começar o jogo!")

print("----------------------O número é de 1 a 50!---------------------------")

nome = input("Escolha um nick: ")

while True:

    nivel = input("Fácil(f), Médio(m) ou Difícil(d): ").lower()

    chances = 0 

    if nivel == "f" or nivel == "fácil":

        print(f"{nome} entrou no nível fácil, e possui 15 chances")

        chances = 15

        pontos = 11

    elif nivel == "m" or nivel == "médio":

        print(f"{nome} entrou no modo médio, possui 10 chances!")

        chances = 10

        pontos = 18

    else:

        print(f"Modo difícil selecionado, se prepare com 7 chances {nome}!!!")

        chances = 7

        pontos = 25

    numero = random.randint(1, 50)

    for chance_atual in range(1, chances + 1):

        print("--------------------------------------")

        pontos -= 1 

        tentativa = int(input(f"Chances {chance_atual} de {chances}, tente: "))

        if tentativa > numero:

            print("------------------------------------")

            print(f"Seu número é MENOR que {tentativa}!")

        elif tentativa < numero:

            print("------------------------------------")

            print(f"Seu número é MAIOR que {tentativa}!")

        else:

            print("------------------------------------")

            print(f"Você acertou, o número era: {numero} e ganhou {pontos} pontos, parabens {nome}!!!")

            print("------------------------------------")

            print(f"Muito bem {nome}! Vamos mais uma rodada?\n")

            break

        if chance_atual == chances // 2:

            print("------------------------------------")

            print(f"Já está na metade! Continue tentando {nome}!!!!")

        if chance_atual == chances - 1:

            print("------------------------------------")

            print(f"Você está na ultima tentativa, iras morrer {nome}!!!!!!")

    else:

        print("------------------------------------")

        print(f"{nome} ultrapassou o limite de chances e morreu, o número era: {numero}!")

        print("------------------------------------")

        print(f"que tal na proxima {nome}, deseja jogar dnv?\n")

    jogar_dnv = input("sim(s) ou não(n): ").lower()

    if jogar_dnv == "s" or jogar_dnv == "sim":

        print("Carregando...")

        print("------------------------------------")

    else:

        break        
