# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = soma = 0 # Atribuir zero ao num neste caso, é considerado uma "guambiarra", há um método de fazer a repetição sem precisar disso (aula 15)
cont = -1
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {cont} números e a soma é {soma}!')
