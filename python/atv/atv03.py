#03 - verificador de idade e autorização 

print("Bem vindo a balada python, vamos ver se você entra ou não!!!") 

print("___________________________________________\n")

idade = input("Sua idade:")

if (int(idade)) >= 18: 

    print("Entra na balada!")

else:

    if (int(idade)) < 16:

        print("Você é uma criança, saia daqui mn!")
    else:

        print("Tem autorização ? (S/N)")

        print("Resposta:")

        autorizacao = input()
    
        if autorizacao == "s" or autorizacao == "S":
            print("Entra então na balada com autorização dos papis!!!")
        else:

            print("Sai daqui mn, volta quando tiver 18 anos ou autorização dos papis!!!")
