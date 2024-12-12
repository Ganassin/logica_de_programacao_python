# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

from time import sleep

dados = dict()
pessoas = list()

while True:

    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dados['sexo'] not in 'MF':
            print('\nO sexo deve ser M para masculino ou F para feminino!')
            print()
        else:
            break
    dados['idade'] = int(input('Idade: '))

    pessoas.append(dados.copy())
    dados.clear()

    print()
    while True:
        resposta = str(input('Deseja adicionar mais dados? [S/N] ')).strip().upper()
        if resposta not in 'SN':
            print('\nErro! Digite "S" para sim ou "N" para não')
            print()
        else:
            break
    print()
    if resposta == 'N':
        break

sleep(0.5)
print('Analisando...')
sleep(1)

# Qnt de pessoas cadastradas
qnt_pessoas = len(pessoas)
print(f' - No total {qnt_pessoas} foram cadastradas!')
sleep(1)

# Idade média
sum_idade = 0
for p in pessoas:
    sum_idade += p['idade']

media_idade = sum_idade/qnt_pessoas

print(f' - A média de idade das pessoas cadastradas é {round(media_idade, 2)} anos!')
sleep(1)

# Lista de mulheres
mulheres = list()
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])

print(f' - Há {len(mulheres)} mulheres cadastradas, sendo ela(s): {mulheres}')
sleep(1)

# Lista de pessoas com idade a cima da média
for p in pessoas:
    if p['idade'] > media_idade:
        print(' - Lista de pessoas com idade a cima da média:')
        for k, v in p.items():
            print(f'   {k} = {v};', end='')
