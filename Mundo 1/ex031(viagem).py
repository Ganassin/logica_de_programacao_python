# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância a ser percorrida na viagem? '))

if dist <= 200:
    print(f'Você deverá pagar a taxa 1, de R$ {dist*0.5:.2f}')
else:
    print(f'Você deverá pagar a taxa 2, de R$ {dist*0.45:.2f}')