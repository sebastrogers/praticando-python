import re

nome_completo_ano_nasc = input("Digite seu nome completo e ano de nascimento (ex: João Silva - 1990): ")
padrao = r'(\w) (\w) - \d{4}$'

resultado = re.search(padrao, nome_completo_ano_nasc)
if resultado:
    primeiro_nome = resultado.group(1)
    sobrenome = resultado.group(2)
    ano_nascimento = resultado.group(3)
    print(f"Primeiro nome: {primeiro_nome}")
    print(f"Sobrenome: {sobrenome}")
    print(f"Ano de nascimento: {ano_nascimento}")
else:
    print("Formato inválido! Certifique-se de digitar no formato: João Silva - 1990")
