tupla = 'Anel', 'Caderno', 'Regua', 'Papel', 'Planta', 'Mesa', 'Mouse', 'Notebook'

vogais = ''

for palavra in tupla:

    for letra in palavra:
        if letra in 'aeiouAEIOU' and letra.upper() not in vogais:
           vogais = vogais + f'{letra} '.upper()

    print(f'{palavra}'.ljust(10, '.'), f'tem as seguintes vogais: {vogais}')
    vogais = ''