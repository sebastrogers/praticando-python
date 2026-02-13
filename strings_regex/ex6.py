# texto = input("Digite um texto: ")
# palavra_substituida = input("Digite a palavra a ser substituída: ")
# nova_palavra = input("Digite a nova palavra: ")

# texto_modificado = texto.replace(palavra_substituida, nova_palavra)
# print("Texto modificado: ", texto_modificado)

import re

texto = input("Digite o texto a ser revisado: ")  
palavra_antiga = input("Qual palavra deseja substituir? ")  
palavra_nova = input("Qual a nova palavra? ")  

nova_frase = re.sub(rf'\b{palavra_antiga}\b', palavra_nova, texto)
print(nova_frase)