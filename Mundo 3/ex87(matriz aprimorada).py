matriz = [[], [], []]
for linha in range(0, 3):
    matriz[linha] = [int(input(f'Digite um valor {linha}x{cont}: ')) for cont in range(0, 3)]

print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

pares = []
soma_terceira_coluna = 0
maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])

        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

        if linha == 1 and coluna == 0:
            maior = matriz[linha][coluna]
        elif linha == 1 and matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]

print(f'\nA soma de todos os valores pares {pares} é: {sum(pares)}')
print(f'\nA soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'\nO mior valor da linha 2 é {maior}')