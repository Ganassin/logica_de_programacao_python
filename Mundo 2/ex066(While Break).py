# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = cont = soma = 0

print('\nDigite 999 caso queria encerrar o programa!\n')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números digitados é {soma:^10}!')
