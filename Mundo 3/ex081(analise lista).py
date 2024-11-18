valores = []
escolha = ''

# Recebe valores na lista até que o usuário deseje parar
while True:
    valores.append(int(input('Digite um valor: ')))

    escolha = str(input('Deseja continuar digitando? [S/N] \n')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('Digite S (sim) ou N (não): \n')).strip().upper()
    if escolha in 'Nn':
        break

# Mostra quantos valores tem na lista
print(f'\nForam digitados {len(valores)} números!')
# Mostra a lista em ordem decrescente
print(f'Esses números em ordem decrescente são: {sorted(valores, reverse=True)}') # OU valores.sort(reverse=True)

# Analise se há o valor 5 na lista e em que posição está.
if 5 in valores:
    valores_cinco = [pos for pos, v in enumerate(valores) if v == 5]
    print(f'O valor 5 foi digitado na(s) posição(ões) {valores_cinco} da lista!')
else:
    print('O valor 5 não foi digitado!')