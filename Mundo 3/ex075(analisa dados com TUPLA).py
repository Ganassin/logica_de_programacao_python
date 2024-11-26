# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

'''
numeros = (int(input('Digite um valor de 1 a 10: ')),
           int(input('Digite outro valor de 1 a 10: ')),
           int(input('Digite outro valor de 1 a 10: ')),
           int(input('Digite outro valor de 1 a 10: ')),
           int(input('Digite o último valor de 1 a 10: ')))
print(f'\nVoce digitou os valores {numeros}')

cont9 = pos3 = 0
pares = ''
for pos, x in enumerate(numeros):
    # Conta os 9
    if x == 9:
        cont9 += 1

    if pos3 == 0:
        if x == 3:
            pos3 = pos
    # Adiciona os pares em uma string
    if x % 2 == 0:
        pares += f'{numeros[pos]} '

# Mostra quantos 9 foram digitados, se foi digitado
if 9 in numeros:
    print(f'O número 9 aparece {cont9} OU {numeros.count(9)} vezes!') # No caso no COUNT(9), não precisa do if a cima
else:
    print('Você não digitou o número 9!')

# Mostra a posição do primeiro 3 caso pelo menos um 3 tenha sido digitado
if 3 not in numeros:
    print('O número 3 não foi digitado!')
else:
    print(f'O número 3 aparece pela primeira vez na posição {pos3+1} OU {numeros.index(3)+1}')

# Mostra os pares caso existam
if pares != '':
    print(f'Os numeros pares são: {pares}')
else:
    print('Não há números pares!')
'''
# Código com menos ifs
numeros = (int(input('Digite um valor de 1 a 10: ')),
           int(input('Digite outro valor de 1 a 10: ')),
           int(input('Digite outro valor de 1 a 10: ')),
           int(input('Digite outro valor de 1 a 10: ')),
           int(input('Digite o último valor de 1 a 10: ')))
print(f'\nVoce digitou os valores {numeros}')

# Mostra quantos 9 foram digitados, se foi digitado ----------------------------------------------------
if 9 in numeros:
    print(f'O número 9 aparece {numeros.count(9)} vezes!')
else:
    print('Você não digitou o número 9!')

# Mostra a posição do primeiro 3 caso pelo menos um 3 tenha sido digitado -----------------------------
if 3 not in numeros:
    print('O número 3 não foi digitado!')
else:
    print(f'O número 3 aparece pela primeira vez na posição {numeros.index(3)+1}')

# Mostra os pares caso existam -----------------------------------------------------------------------
pares = ''
for x in numeros:
    # Adiciona os pares em uma string
    if x % 2 == 0:
        pares += f'{x} '

if pares != '':
    print(f'Os numeros pares são: {pares}')
else:
    print('Não há números pares!')