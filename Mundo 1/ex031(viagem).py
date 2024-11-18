dist = float(input('Qual a distância a ser percorrida na viagem? '))
if dist <= 200:
    print(f'Você deverá pagar a taxa 1, de R$ {dist*0.5:.2f}')
else:
    print(f'Você deverá pagar a taxa 2, de R$ {dist*0.45:.2f}')