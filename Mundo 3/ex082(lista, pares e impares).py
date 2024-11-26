# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

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

valores_pares = [v for v in valores if v % 2 == 0]
valores_impares = [v for v in valores if v % 2 != 0]

print(f'\nOs valores digitados foram {valores}!\n'
      f'  - Sendo {valores_pares} os pares!\n'
      f'  - E {valores_impares} os ímpares!')
