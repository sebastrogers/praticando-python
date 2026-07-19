# Lista atual de convidados: ['Ana', 'Pedro', 'Carlos']
# Digite o nome do novo convidado: João
# Digite a posição na qual deseja inserir o convidado: 2

lista = ["Ana", "Pedro", "Carlos"]
convidado = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))

novaLista = lista
novaLista.insert(posicao, convidado)

print(f'Lista atualizada de convidados: {novaLista}')