# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

# recebe o numero do usuário
num = int(input('Digite um número que queira saber o seu fatorial: '))

print(f'{num}! =', end='')

# Faz o print de todos os números usados no fatorial
c = num
while c > 1:
    print(f' {c} x',end='')
    c -= 1

# Calcula o fatorial
print(f' 1 = {factorial(num)}')
