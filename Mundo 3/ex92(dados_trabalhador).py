# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = {
    'Nome': str(input('Digite o nome: ')),
    'Sexo': str(input('Sexo [M/F]:  ')).strip().upper(),
    'Nascimento': int(input('Ano de nascimento: '))
}

dados['Idade'] = datetime.now().year - dados['Nascimento']
print('Caso não tenha carteira assinada digite 0')
dados['Ctps'] = int(input('Digite o número da CTPS: '))

# adiciona ano de contratação e salário se há ctps
if dados['Ctps'] != 0:
    dados['Ano_contratacao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario: '))

    # Adiciona a idade de aposentadoia (só se tiver ctps)
    if dados['Sexo'] == 'M':
        dados['Idade_aposentadoria'] = (dados['Ano_contratacao'] + 35) - dados['Nascimento']
    elif dados['Sexo'] == 'F':
        dados['Idade_aposentadoria'] = (dados['Ano_contratacao'] + 30) - dados['Nascimento']
    else:
        dados['Idade_aposentadoria'] = 'Sexo não identificado!'

print(dados)