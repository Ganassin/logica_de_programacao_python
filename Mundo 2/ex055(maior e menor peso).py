# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000

for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa?: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'\nO maior peso é {maior}')
print(f'e o menor peso é {menor}')