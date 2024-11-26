# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = [int(input('Digite o 1º número: ')),
           int(input('Digite o 2º número: ')),
           int(input('Digite o 3º número: ')),
           int(input('Digite o 4º número: ')),
           int(input('Digite o 5º e último número: '))]

maximo = max(valores)
minimo = min(valores)

pos_max = pos_min = ''
for pos, v in enumerate(valores):
    if v == maximo:
        pos_max += f'{pos}...'
    if v == minimo:
        pos_min += f'{pos}...'

print(f'\nO maior valor é {maximo}, que está na posição {pos_max}')
print(f'O menor valor é {minimo}, que está na posição {pos_min}')

'''-------------------------- OU ------------------------------'''
''' Usando uma técnica chamada "COMPREENÇÃO DE LISTAS", que é basicamente a criação de listas a partir de listas '''

# Armazena em uma lista a posição (pos) do FOR, se o valor (v) do FOR for igual ao máximo ou do mínimo
pos_maior = [pos for pos, v in enumerate(valores) if v == maximo]
pos_menor = [pos for pos, v in enumerate(valores) if v == minimo]

print(f'\nO maior valor é {maximo}, que está na posição {pos_maior}')
print(f'O menor valor é {minimo}, que está na posição {pos_menor}')
