#02 - calculadora básica

print("Bem vindo!!!!, aqui é uma calculadora, ok?")

n1 = float(input("Digite seu primeiro número: "))

n2 = float(input("Dígite seu primeiro número: "))

while True: 

    escolha = input("Qual operação você gostaria de realizar: \n+ para somar \n- para subtrair \n * para multiplicar \n / para dividir \n\n Digite sair para sair: \n").lower().strip()

    if escolha == "+":
        print(f"Seu resultado:{n1 + n2}.") 

    elif escolha == "-":
        print(f"Seu resultado:{n1 - n2}.") 

    elif escolha == "*":
        print(f"Seu resultado:{n1 * n2}.") 

    elif escolha == "/":
        print(f"Seu resultado:{n1 / n2}.")

    elif escolha == "sair":
        print("Você saiu do loop!")

        break

    else:
        print("Caracter invalido, use uma das opções seu animal!")

        


