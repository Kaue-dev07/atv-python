#01w - acertar numero de 1 a 20 com while
#nessa situação o melhor é usar for, oq eu fiz acima, pois sabemos o numeros de chances.

import random

numero = random.randint(1, 20)

print("Você tem 5 chances para acertar um número de 1 a 20.")

print("-----------------------------------------------------")

chances = 0

while True:

    tentativa = int(input("Tente: "))

    chances += 1

    print("------------------------------------")

    print(f"Você está na tentativa {chances}!")

    if tentativa > numero:

        print("------------------------------------")

        print(f"Seu número é menor que {tentativa}!")

    elif tentativa < numero:

        print("------------------------------------")

        print(f"Seu número é maior que {tentativa}!")

    else:

        print("------------------------------------")

        print(f"Você acertou, o número era {numero}!")

        break

    if chances == 5:

        print(f"Você chegou a 5 tentativas e foi explodido! O número era {numero}")

        break