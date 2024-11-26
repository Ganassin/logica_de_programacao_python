# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[], [], []]
for linha in range(0, 3):
    matriz[linha] = [int(input(f'Digite um valor {linha}x{cont}: ')) for cont in range(0, 3)]

print(f'{matriz[0]:}\n{matriz[1]}\n{matriz[2]}')