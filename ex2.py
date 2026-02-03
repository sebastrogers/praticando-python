# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir 
# três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, 
# o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
# Se algum valor for negativo, mostre uma mensagem informando o erro.

atv1 = int(input("Informe os dias para a atividade A: "));
atv2 = int(input("Informe os dias para a atividade B: "));
atv3 = int(input("Informe os dias para a atividade C: "));

if atv1 <= 0 or atv2 <= 0 or atv3 <= 0:
    print("Os dias não podem ser negativos")
else:
    print(f"Os dias de atividade total são: {atv1 + atv2 + atv3}")