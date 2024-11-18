n = cont = soma = 0

print('\nDigite 999 caso queria encerrar o programa!\n')
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números digitados é {soma:^10}!')
