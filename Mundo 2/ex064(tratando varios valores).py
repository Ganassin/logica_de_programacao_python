num = soma = 0 # Atribuir zero ao num neste caso, é considerado uma "guambiarra", há um método de fazer a repetição sem precisar disso (aula 15)
cont = -1
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {cont} números e a soma é {soma}!')
