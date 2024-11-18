numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha_numero = int(input('\nEscolha um número de 1 a 20 e o veja escrito por extenso: '))
    while escolha_numero<0 or escolha_numero>20:
        escolha_numero = int(input('\nTente novamente! Escolha um número de 1 a 20: '))

    print(f'Você escolheu o {escolha_numero} que por extenso é : {numeros[escolha_numero]}')

    continua = str(input('Você quer continuar? [S/N] ')).strip().upper()
    while continua not in 'SN':
        continua = str(input('Inválido! [S/N]? ')).strip().upper()
    if continua == 'N':
        break
print('\nAté mais!!!')