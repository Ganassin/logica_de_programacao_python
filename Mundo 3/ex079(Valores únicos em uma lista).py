# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# Lista com todos os valores digitados
valores = []
# Lista apenas com os valores únicos, não repetidos
valores_unicos = []
# Lista com apenas os valores repetidos (dig. mais de uma vez)
valores_repetidos = []

# Vai adicionando valores até o usuário responder não[N]
while True:
    numero = int(input('Digite um valor: '))
    # Adiciona o numero na lista "valores"
    valores.append(numero)

    # Testa se o numero já foi digitado ou não
    if numero not in valores_unicos:
        # Add em "valores_unicos" o número dig. pela 1º vez
        valores_unicos.append(numero)
    else:
        print('Valor duplicado, não vou adicionar!!!')
        if numero not in valores_repetidos:
            # Add em "valores_repetidos" o número repetido, se ele não foi adicionado antes!
            valores_repetidos.append(numero)

    # Teste para ver se o usuário que continuar digitando numeros ou não
    escolha = str(input('Quer adicionar mais valores à lista? [S/N] ')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('An? Sim[S] ou Não[N]? ')).strip().upper()
    if escolha == 'N':
        break

# Mosta os valores digitados em ordem crescente, sem contar os repetidos
print(f'\nOs valores digitados foram: {sorted(valores_unicos)}')
# Mosta os valores que foram dig. mais de uma vez
print(f'\nOs valore(s) {sorted(valores_repetidos)} foi(ram) digitado(s) mais de uma vez!')

# Mostra a posição de cada um dos valores que foram digitados mais de uma vez
    # Cada valor da lista de repetidos é conferido dentro da lista de todos os val. digitados
    # e a pos. do repetido é armazenada
pos_repetidos = []
for pos1, v1 in enumerate(sorted(valores_repetidos)):

    for pos2, v2 in enumerate(valores):
        if v1 == v2:
            pos_repetidos.append(pos2+1)
    ''' OU com LIST COMPREHENSION:      
    pos_repetidos = [pos2 for pos2, v2 in enumerate(valores) if v1 == v2]'''

    print(f'O valor {v1} apareceu nas posições {pos_repetidos}!')
    pos_repetidos = []
