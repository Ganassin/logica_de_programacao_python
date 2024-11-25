# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

aleatorio = randint(0, 5)
num = int(input('Escolha um número inteiro de 1 a 5: '))

if num == aleatorio:
    print('Parabéns, você acertou!!!')
else:
    print('Não foi dessa vez!')

