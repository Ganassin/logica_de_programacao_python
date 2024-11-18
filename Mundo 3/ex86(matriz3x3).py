matriz = [[], [], []]
for linha in range(0, 3):
    matriz[linha] = [int(input(f'Digite um valor {linha}x{cont}: ')) for cont in range(0, 3)]

print(f'{matriz[0]:}\n{matriz[1]}\n{matriz[2]}')