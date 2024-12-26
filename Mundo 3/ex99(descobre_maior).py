# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior (*num):
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='')
    print(f'(Foram informados {len(num)} ao todo)')
    print(f'O maior valor informado foi {max(num)}')

maior(1,6,32,4,65,5,4,3,)
