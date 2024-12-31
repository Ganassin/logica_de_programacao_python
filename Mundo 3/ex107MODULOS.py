# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from modulos import moeda_107

preco = float(input('\nDigite um valor: '))

print(f'\nO dobro é {moeda_107.dobro(preco)} e a metade é {moeda_107.metade(preco)}!')
print(f'O valor com um desconto de 15% é {moeda_107.diminuir(preco, 15)}')
print(f'O valor com um aumento de 30% é {moeda_107.aumentar(preco, 30)}')