velocidade = float(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('!'*5, f' Você foi multado em R$ {(velocidade-80)*7:.2f}', '!'*5)
