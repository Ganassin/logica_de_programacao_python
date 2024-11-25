# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''from math import floor, trunc

n1 = float(input('Digite um número: '))
print(f'A parte inteira do número {n1} é {floor(n1)} ou {trunc(n1)}') #floor() tras a parte inteira de um float
'''

# Outra forma, sem importação
n1 = float(input('Digite um número: '))
print(f'A parte inteira do número {n1} é {int(n1)}')