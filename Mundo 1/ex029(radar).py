# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('!'*5, f' Você foi multado em R$ {(velocidade-80)*7:.2f}', '!'*5)
else:
    print("Velocidade permitida!")
