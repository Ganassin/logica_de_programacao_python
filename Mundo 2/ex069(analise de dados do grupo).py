# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

continuar = sexo = ''
idade = cont_18 = cont_masc = cont_fem = 0
while True:
    # Menu com título e recebe informações de sexo e idade
    print('-'*30,'\n   CADASTRE UMA PESSOA   \n', '-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 30)

    # Faz as contagens de maiores de idade, homens e mulheres com mais de 20 anos
    if idade >= 18:
        cont_18 += 1
    if sexo in 'Mm':
        cont_masc += 1
    if sexo in 'Ff' and idade < 20:
        cont_fem += 1

    # Valida se o usuário quer ou não continuar
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer contiunuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break

# Fora do WHILE, mostra os resultados
print(f'\nTotal de pessoas com mais de 18 anos: {cont_18}')
print(f'Total de homens: {cont_masc}')
print(f'Total de mulheres com menos de 20 anos: {cont_fem}')