numeros = [] # lista base para receber numeros digitados
numeros_separados = [[], []] # lista final para organizar os numeros digitados

for cont in range(0, 7):
    numeros.append(int(input(f'Digite o {cont+1}º valor: ')))

    if numeros[cont] % 2 == 0 and numeros[cont] not in numeros_separados[0]: # se resto da div. por 2 é zero e não está na lista organizada ainda
        numeros_separados[0].append(numeros[cont])                           # adiciona na primeira lista denttro da lista organizada.
    elif numeros[cont] % 2 != 0 and numeros[cont] not in numeros_separados[1]:
        numeros_separados[1].append(numeros[cont])

print(f'Os numeros pares são: {sorted(numeros_separados[0])}')
print(f'Os numeros inpares são: {sorted(numeros_separados[1])}')
