# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar 
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

'''saque = int(input('Qual valor quer sacar? R$'))

cinquenta = saque // 50
vinte = (saque-(cinquenta*50)) // 20
dez = (saque-(cinquenta*50)-(vinte*20)) // 10
um = (saque-(cinquenta*50)-(vinte*20)-(dez*10) // 1)

if cinquenta > 0:
    print(f'{cinquenta} notas de R$ 50,00;')
elif vinte > 0:
    print(f'{vinte} notas de R$ 20,00;')
elif dez > 0:
    print(f'{dez} notas de R$ 10,00;')
elif um > 0:
    print(f'{um} notas de R$ 1,00!')'''

saque = int(input('Qual valor quer sacar? R$ '))

cedula_atual = 50
cont_cedulas = 0
while True:
    if saque >= cedula_atual:
        saque -= cedula_atual
        cont_cedulas += 1
    else:
        if cont_cedulas != 0:
            print(f'Total de {cont_cedulas} de R${cedula_atual}')
        if cedula_atual == 50:
            cedula_atual = 20
            cont_cedulas = 0
        elif cedula_atual == 20:
            cedula_atual = 10
            cont_cedulas = 0
        elif cedula_atual == 10:
            cedula_atual = 1
            cont_cedulas = 0
        if saque == 0:
            break
