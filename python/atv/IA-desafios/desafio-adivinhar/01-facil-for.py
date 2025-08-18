#01f - acertar numero de 1 a 20 com for
#nessa situação que a gente ja sabe o numero de chances que o usuario tem, o certo é usar "for"

import random

numero = random.randint(1, 20)

print("Você tem 5 chances para acertar um número de 1 a 20.")

print("-----------------------------------------------------")

chances = 0

for chances in range(5):

    tentativa = int(input(f"Tentativa {chances + 1} de 5, Tente: "))

    if tentativa > numero:

        print("------------------------------------")

        print(f"Seu número é menor que {tentativa}!")

    elif tentativa < numero:

        print("------------------------------------")

        print(f"Seu número é maior que {tentativa}!")

    else:

        print("------------------------------------")

        print(f"Você acertou, o número era: {numero}")

        break

else:

    print("------------------------------------")

    print(f"Você ultrapassou o limite de chances e morreu, o número era: {numero}!")

