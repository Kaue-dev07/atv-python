#você digita seu nome e bota uma mensagem que fica salva no terminal

import os

mensagens = []
 
nome = input("nome: ")

while True:

    os.system('cls')

    if len(mensagens)>0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

            print("_______________________")

    texto =  input("Digite sua mensagem: ")
    if texto == "fim":
         break

    mensagens.append({
    "nome": nome,
    "texto": texto
    
})
