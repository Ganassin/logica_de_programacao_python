maior = menor = soma = cont = 0


escolha = 'S'
while escolha == 'S':
    num = int(input('Digite um valor: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    soma += num
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

print(f'\nVocê digitou {cont} números e a média foi de {soma/cont:.2f}')
print(f'O maior valor foi {maior} e o menor {menor}!')
