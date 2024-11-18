# importação da biblioteca para pegar informações de data do sistema e criação da var com o ano atual
from datetime import date
ano_atual = date.today().year

# Criação dos contadores de maiores e menores de idade
cont_maior = 0
cont_menor = 0

# Deixa o usuário escolhar a idade em que uma pessoa é considerada maior.
maioridade = int(input('Qual a idade de maioridade onde você mora?: '))

for c in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {c}º pessoa nasceu?: '))      # Recebe um ano digitado pelo usuário
    if (ano_atual-ano_nascimento) >= maioridade:
        cont_maior += 1 # Se a idade for maior ou igual à idade que o usuário escolheu, adiciona 1 no contador de maiores de idade
    elif (ano_atual-ano_nascimento) < maioridade:
        cont_menor += 1 # Se a idade for menor à idade que o usuário escolheu, adiciona 1 no contador de menores de idade

print(f'\nAo todo temos {cont_maior} pessoas maiores de idade')
print(f'e {cont_menor} pessoas menores de idade!')