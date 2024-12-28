# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from modulos import moeda_108

preco = float(input('\nDigite um valor: R$ '))

print(f'\nO dobro de {moeda_108.moeda(preco)} é {moeda_108.moeda(moeda_108.dobro(preco))} e a metade é {moeda_108.moeda(moeda_108.metade(preco))}!')
print(f'O valor com um desconto de 15% é { moeda_108.moeda(moeda_108.diminuir(preco, 15)) }')
print(f'O valor com um aumento de 30% é { moeda_108.moeda(moeda_108.aumentar(preco, 30)) }')