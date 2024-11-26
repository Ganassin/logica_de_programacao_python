# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número 
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando 
# no final quantos palpites foram necessários para vencer.

# VERSÃO 2.0 DO EXERCÍCIO 28
import random

print('Tente adivinhar o número de 0 a 10 em que estou pensando...')
# sorteia um número de 1 a 10
num = random.randint(0, 10)

palpite = int(input('Qual o seu palpite? '))
tentativas = 1
while palpite != num:
    if palpite < num:
        print('Mais... Tente outra vez!')
    elif palpite > num:
        print('Menos... Tente outra vez!')
    palpite = int(input('\nQual o seu palpite? '))
    tentativas += 1

print(f'\nVocê acertou com {tentativas} tentativas!')
print('=-'*15)
