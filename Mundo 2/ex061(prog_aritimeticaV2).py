# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

''' Igual ao exercício 51, porém com WHILE '''

print('='*40)
texto = '10 termos de uma PA'.center(40) # centraliza o texto dentro de 40 caracteres
print(texto)
print('='*40)

termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

c = 0
while c < 10:
    print(f'{termo+(razao*c)} -> ',end='')
    c += 1
print('Pausa!')