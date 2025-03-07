# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print('='*40)
texto = '10 termos de uma PA'.center(40) # centraliza o texto dentro de 40 caracteres
print(texto)
print('='*40)

termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

for c in range(termo, termo+(10*razao), razao):
    print(c, end=' -> ')
print('ACABOU')