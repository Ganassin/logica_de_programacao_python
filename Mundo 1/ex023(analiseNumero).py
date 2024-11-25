# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número: '))

# 1. Divide o número por (1, 10, 100 e 1000) pegando apenas a parte inteira dessa divisão. (move a vírgula para a esquerda)
# 2. Depois pega o resto do resultado anterior dividido por 10
u = (num // 1) % 10
d = (num // 10) % 10
c = (num // 100) % 10
m = (num // 1000) % 10

print(f'Unidade {u}\n'
      f'Dezena {d}\n'
      f'Centena {c}\n'
      f'Milhar {m}')