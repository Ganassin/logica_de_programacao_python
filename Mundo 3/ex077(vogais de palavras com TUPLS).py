# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = 'Anel', 'Caderno', 'Regua', 'Papel', 'Planta', 'Mesa', 'Mouse', 'Notebook'

vogais = ''

for palavra in tupla:

    for letra in palavra:
        if letra in 'aeiouAEIOU' and letra.upper() not in vogais:
           vogais = vogais + f'{letra} '.upper()

    print(f'{palavra}'.ljust(10, '.'), f'tem as seguintes vogais: {vogais}')
    vogais = ''