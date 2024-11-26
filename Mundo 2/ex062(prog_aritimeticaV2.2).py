# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

''' Melhoria do exercício 61 '''

print('='*40)
texto = '10 termos de uma PA'.center(40) # centraliza o texto dentro de 40 caracteres
print(texto)
print('='*40)

termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

'''c = 0
while c < 10:
    print(f'{termo} -> ',end='')
    termo += razao
    c += 1
print('Pausa!')

n = int(input('Quantos termos você quer mostrar a mais? '))
cont = 10 + n
c = 0
while n != 0:
    while c < n:
        print(f'{termo} -> ', end='')
        termo += razao
        c += 1
    print('Pausa!')
    c = 0
    n = int(input('Quantos termos você quer mostrar a mais? '))
    cont += n
print(f'\nProgressão aritimética finalizada com {cont} termos mostrados!')'''

# OU ############################## VERSÃO MENOR ###################################################################

c = 0
mais = 10
cont = 0
while mais != 0:
    while c < mais:
        print(f'{termo} -> ',end='')
        termo += razao
        c += 1
    print('Pausa!')
    cont += mais
    c = 0
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'\nProgressão aritimética finalizada com {cont} termos mostrados!')
