# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no 
# mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
# Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando 
# qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.



produto_maca = int(input("Digite a quantidade de maçãs vendidas: "));
produto_banana = int(input("Digite a quantidade de bananas vendidas: "));

if produto_maca > produto_banana:
    print("As maçãs tiveram mais vendas");
elif produto_maca < produto_banana:
    print("As bananas tiveram mais vendas");
else:
    print("As vendas foram iguais");