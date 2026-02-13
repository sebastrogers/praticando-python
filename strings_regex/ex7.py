import re

nome_cliente = input("Digite o nome do cliente: ")
padrao = r'^[A-Z][a-zA-Z]*$'
if re.match(padrao, nome_cliente):
    print("Nome válido!")
else:        
    print("Nome inválido! O nome deve começar com letra maiúscula e conter apenas letras.")
