# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from time import sleep

ano = int(input('Digite um ano para saber se é bissexto: '))

print('\n--- Antes um pouco de informação ---\n'
      'O ano bissexto acontece a cada\nquatro anos e tem duração de 366\ndias,'
      'diferentemente dos demais\nque têm 365 dias.')

sleep(1)
print('\nCalculando...')
sleep(3)

if ano % 4 == 0:
    print('\nAno Bissexto!')
else:
    print('\nAno normal!')