#01 - Furto do banco

import random

senha = random.randint(0, 9)

print("Você está roubando um banco e tem 3 chances para acertar a senha de 0 a 9.")

tentativas = 0

while True:

    numero = int(input("Tente um número: "))

    tentativas += 1

    print("Outra tentaiva!")

    if numero == senha:

        print("Você é um baita de um cagão e acertou a senha")

        break

    if tentativas == 3:

        print("Você errou a senha e foi preso")

        break
