numero = int(input("Digite um número: "))

dobro = numero * 2

metade = numero / 2

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i 

print(f"O dobro do seu número é {dobro}, a metade é {metade} e o fatorial é {fatorial}.")