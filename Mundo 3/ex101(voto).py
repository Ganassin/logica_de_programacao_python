# Exercício Python 101: Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto 
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto (ano):
    from datetime import datetime

    hoje = datetime.now().year
    idade = hoje - ano

    if idade >= 18:
        return f'Com {idade} anos, o voto é Obrigatório!'
    elif 16 <= idade < 18:
        return f'Com {idade} anos, o voto éOpcional!'
    else:
        return 'Negado!'

ano = int(input('Ano de nascimento: '))
print(f'A sua situação eleitoral é: {voto(ano)}')